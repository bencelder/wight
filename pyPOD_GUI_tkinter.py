import Tkinter as tk
import webbrowser
top = tk.Tk()

def visitURL(url):
   webbrowser.open(url)

# create a menu
menu = tk.Menu(top)
top.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Preferences", command=None)


link = "http://apod.nasa.gov/apod/image/1309/sgra_gasChandra.jpg"
linkname = "NASA Photo Of The Day"
B = tk.Button(top, text =linkname, command = lambda:visitURL(link))
B.pack()
top.mainloop()
