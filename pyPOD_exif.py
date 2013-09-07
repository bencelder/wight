import os
import wx
from wx.lib.pubsub import Publisher
 
pil_flag = False
pyexif_flag = False
 
try:
    import exif
    pyexif_flag = True
except ImportError:
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS
        pil_flag = True
    except ImportError:
        pass
 
#----------------------------------------------------------------------
def getExifData(photo):
    """
    Extracts the EXIF information from the provided photo
    """
    if pyexif_flag:
        exif_data = exif.parse(photo)
    elif pil_flag:
        exif_data  = {}
        i = Image.open(photo)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value
    else:
        raise Exception("PyExif and PIL not found!")
    return exif_data
 
#----------------------------------------------------------------------
def getPhotoSize(photo):
    """
    """
    photo_size = os.path.getsize(photo)
    photo_size = photo_size / 1024.0
    if photo_size > 1000:
        # photo is larger than 1 MB
        photo_size = photo_size / 1024.0
        size = "%0.2f MB" % photo_size
    else:
        size = "%d KB" % photo_size
    return size
 
########################################################################
class Photo:
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, photo):
        """Constructor"""
        self.exif_data = getExifData(photo)
        self.filename = os.path.basename(photo)
        self.filesize = getPhotoSize(photo)
 
 
########################################################################
class MainPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent, photo):
        """Constructor"""
        wx.Panel.__init__(self, parent)
 
        # dict of Exif keys and static text labels
        self.photo_data = {"ApertureValue":"Aperture", "DateTime":"Creation Date",
                           "ExifImageHeight":"Height", "ExifImageWidth":"Width",
                           "ExposureTime":"Exposure", "FNumber":"F-Stop",
                           "Flash":"Flash", "FocalLength":"Focal Length", 
                           "ISOSpeedRatings":"ISO", "Model":"Camera Model", 
                           "ShutterSpeedValue":"Shutter Speed"}
 
        # TODO: Display filesize too!
        self.exif_data = photo.exif_data
        self.filename = photo.filename
        self.filesize = photo.filesize
        Publisher().subscribe(self.updatePanel, ("update"))
 
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.layoutWidgets()
        self.SetSizer(self.mainSizer)
 
    #----------------------------------------------------------------------
    def layoutWidgets(self):
        """
        """
        ordered_widgets = ["Model", "ExifImageWidth", "ExifImageHeight",
                           "DateTime", "static_line",
                           "ApertureValue", "ExposureTime", "FNumber",
                           "Flash", "FocalLength", "ISOSpeedRatings",
                           "ShutterSpeedValue"
                           ]
 
        self.buildRow("Filename", self.filename, "Filename")
        self.buildRow("File Size", self.filesize, "FileSize")
        for key in ordered_widgets:
            if key not in self.exif_data and key != "static_line":
                continue
            if (key != "static_line"):
                self.buildRow(self.photo_data[key], self.exif_data[key], key)
            else:
                print "Adding staticLine"
                self.mainSizer.Add(wx.StaticLine(self), 0, wx.ALL|wx.EXPAND, 5)
 
    #----------------------------------------------------------------------
    def buildRow(self, label, value, txtName):
        """"""
 
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        lbl = wx.StaticText(self, label=label, size=(75, -1))
        txt = wx.TextCtrl(self, value=value, size=(150,-1),
                          style=wx.TE_READONLY, name=txtName)
        sizer.Add(lbl, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(txt, 0, wx.ALL, 5)
        self.mainSizer.Add(sizer)
 
    #----------------------------------------------------------------------
    def updatePanel(self, msg):
        """"""
        photo = msg.data
        self.exif_data = photo.exif_data
 
        children = self.GetChildren()
        for child in children:
            if isinstance(child, wx.TextCtrl):
                self.update(photo, child)
 
    #----------------------------------------------------------------------
    def update(self, photo, txtWidget):
        """"""
        key = txtWidget.GetName()
 
        if key in self.exif_data:
            value = self.exif_data[key]
        else:
            value = "No Data"
 
        if key == "Filename":
            txtWidget.SetValue(photo.filename)
        elif key == "FileSize":
            txtWidget.SetValue(photo.filesize)
        else:
            txtWidget.SetValue(value)
 
########################################################################
class PhotoInfo(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, photo_path):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Image Information")
        photo = Photo(photo_path)
        panel = MainPanel(self, photo)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        sizer.Fit(self)
 
        Publisher().subscribe(self.updateDisplay, ("update display"))
        self.Show()
 
    #----------------------------------------------------------------------
    def updateDisplay(self, msg):
        """
        """
        photo = msg.data
        new_photo = Photo(photo)
        Publisher().sendMessage(("update"), new_photo)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    import wx.lib.inspection
    app = wx.PySimpleApp()
    photo = "C:\Users\Dillon\Documents\GitHub\wight\img.jpg"
    frame = PhotoInfo(photo)
    wx.lib.inspection.InspectionTool().Show()
    app.MainLoop()
