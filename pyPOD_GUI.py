#!/usr/bin/env python

# example treeviewcolumn.py

import pygtk as gtk
pygtk.require('2.0')
#import gtk
import webbrowser

class LinkTitle:
    def title(self,widget,data=None):
        print "Link Name"

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def visit_website(self,url):
        webbrowser.open(url)

    def __init__(self):
        # create a new window
        link = "http://apod.nasa.gov/apod/image/1309/sgra_gasChandra.jpg"
        linkname = "NASA Photo Of The Day"
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        self.button = gtk.Button(linkname)
        self.button.connect_object("clicked", self.visit_website, link)
        self.window.add(self.button)
        self.button.show()
        self.window.show()

    
class TreeViewColumnExample:

    # close the window and quit
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def make_pb(self, tvcolumn, cell, model, iter):
        stock = model.get_value(iter, 1)
        pb = self.treeview.render_icon(stock, gtk.ICON_SIZE_MENU, None)
        cell.set_property('pixbuf', pb)
        return

    def __init__(self):
        # Create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("TreeViewColumn Example")

        #self.window.set_size_request(200, 200)

        self.window.connect("delete_event", self.delete_event)

        # create a liststore with one string column to use as the model
        self.liststore = gtk.ListStore(str,str,'gboolean')

        # create the TreeView using liststore
        self.treeview = gtk.TreeView(self.liststore)

        # create the TreeViewColumns to display the data
        self.tvcolumn = gtk.TreeViewColumn('Car')
        self.tvcolumn1 = gtk.TreeViewColumn('Optimal Lap')

        # add a row with text and a stock item - color strings for
        # the background
        self.liststore.append(['16','1231222322',False])
        self.liststore.append(['06','1231231231',True])
        self.liststore.append(['12','1231321312',False])

        # add columns to treeview
        self.treeview.append_column(self.tvcolumn)
        self.treeview.append_column(self.tvcolumn1)

        # create a CellRenderers to render the data
        self.cellpb = gtk.CellRendererPixbuf()
        self.cell = gtk.CellRendererText()
        self.cell1 = gtk.CellRendererText()

        # set background color property
        self.cellpb.set_property('cell-background', 'yellow')
        self.cell.set_property('cell-background', 'cyan')
        self.cell1.set_property('cell-background', 'pink')


        # add the cells to the columns - 2 in the first
        self.tvcolumn.pack_start(self.cellpb, False)
        self.tvcolumn.pack_start(self.cell, True)
        self.tvcolumn1.pack_start(self.cell1, True)

        # set the cell attributes to the appropriate liststore column
        # GTK+ 2.0 doesn't support the "stock_id" property
        #self.tvcolumn.set_attributes(self.cellpb, stock_id=1)
        self.tvcolumn.set_attributes(self.cell, text=0)
        self.tvcolumn1.set_attributes(self.cell1, text=1,
                                      cell_background_set=2)

        # make treeview searchable
        self.treeview.set_search_column(0)

        # Allow sorting on the column
        self.tvcolumn.set_sort_column_id(0)
        self.tvcolumn1.set_sort_column_id(0)

        # Allow drag and drop reordering of rows
        self.treeview.set_reorderable(True)

        self.window.add(self.treeview)

        self.window.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    tvcexample = LinkTitle()
    main()
