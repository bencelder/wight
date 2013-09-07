import Tkinter as tk
import webbrowser
top = tk.Tk()

def visitURL(url):
   webbrowser.open(url)

def preferences():
    pref = tk.Tk()
    for i in range(0,10):
        var = bool
        l = tk.Checkbutton(pref, text=i,variable=var)
        l.pack()
    l.mainloop()

# create a menu
menu = tk.Menu(top)
top.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Preferences", command=preferences)


link = "http://apod.nasa.gov/apod/image/1309/sgra_gasChandra.jpg"
linkname = "NASA Photo Of The Day"
B = tk.Button(top, text =linkname, command = lambda:visitURL(link))
B.pack()
top.mainloop()


