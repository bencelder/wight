import Tkinter as tk
import webbrowser
top = tk.Tk()

def visitURL(url):
   webbrowser.open(url)

def preferences():
    pref = tk.Tk()
    pref.geometry("300x300")
    counter = 0

    NASAvar = tk.IntVar()
    NASAbox = tk.Checkbutton(pref, text="NASA Photo of the Day",variable=NASAvar)
    NASAbox.pack()


    B = tk.Button(pref, text ="Save", command = lambda:save(pref,NASAvar))
    B.pack()
    pref.mainloop()

def save(pref,NASAvar):
    f = open('preferences.txt', 'w')
    f.write(str(NASAvar))
    pref.destroy()
    

# create a menu
menu = tk.Menu(top)
top.config(menu=menu)

top.title("pyPOD 1.0")
top.geometry("600x600")


filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)



filemenu.add_command(label="Preferences", command=preferences)


link = "http://apod.nasa.gov/apod/image/1309/sgra_gasChandra.jpg"
linkname = "NASA Photo Of The Day"
B = tk.Button(top, text =linkname, command = lambda:visitURL(link))
B.pack()
top.mainloop()

