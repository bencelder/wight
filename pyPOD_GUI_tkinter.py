import Tkinter as tk
import webbrowser
#import pyPOD_timer
import shlex, subprocess
top = tk.Tk()

def visitURL():
    ci = open("currentimage.txt")
    url = ci.readlines()[0]
    webbrowser.open(url)

def preferences():
    global pref
    pref = tk.Tk()
    pref.geometry("300x300")

    global NASAvar
    NASAvar = tk.BooleanVar()
    NASAbox = tk.Checkbutton(pref, text="NASA Photo of the Day",variable=NASAvar)
    NASAbox.pack()

    global NATGEOvar
    NATGEOvar = tk.BooleanVar()
    NATGEObox = tk.Checkbutton(pref, text="NAT GEO Photo of the Day",variable=NATGEOvar)
    NATGEObox.pack()

    B = tk.Button(pref, text ="Save", command = save)
    B.pack()
    pref.mainloop()

def save():
    NASAvarg = NASAvar.get()
    NATGEOvarg = NATGEOvar.get()
    #print NASAvarg
    #print NATGEOvarg
    #print "variable is "+str(NASAvarg)
    f = open('preferences.txt', 'w')
    f.write(str(NASAvarg)+"\n")
    f.write(str(NATGEOvarg)+"\n")
    f.close()
    #pref.destroy()
    

def prnt():
    f = open('preferences.txt', 'w')
    f.write(period.get()+"\n")
    if NASAvar.get():
        f.write(NASAlink+"\n")
    if NATGEOvar.get():
        f.write(NATGEOlink+"\n")
    if VOLvar.get():
        f.write(VOLlink+"\n")
    f.close()
    f = open("refresh.txt","w")
    f.write("1")
    f.close()

def start():
    prnt()
    f = open("stop.txt","w")
    f.write("0")
    f.close()
    command_line = "python pyPOD_timer.py"
    args = shlex.split(command_line)
    p = subprocess.Popen(args)

def stop():
    f = open("stop.txt","w")
    f.write("1")
    f.close()


    
# create a menu
menu = tk.Menu(top)
top.config(menu=menu)

top.title("pyPOD 1.0")
top.geometry("600x600")


filemenu = tk.Menu(menu)
menu.add_cascade(label="Websites", menu=filemenu)

#filemenu.add_command(label="Preferences", command=preferences)


#link = "http://apod.nasa.gov/apod/image/1309/sgra_gasChandra.jpg"
linkname = "Current Image URL"
B = tk.Button(top, text =linkname, command = visitURL)
B.pack()


B = tk.Button(top, text ="START", command = start)
B.pack()
B = tk.Button(top, text ="STOP", command = stop)
B.pack()
B = tk.Button(top, text ="REFRESH", command = prnt)
B.pack()

B = tk.Button(top, text ="Add URL & Name")
B.pack()
URLtxt = tk.StringVar()
e = tk.Entry(top, textvariable=URLtxt)
e.pack()

URLname = tk.StringVar()
e = tk.Entry(top, textvariable=URLname)
e.pack()

global period
period = tk.StringVar(top)
period.set("Period") # default value

w = tk.OptionMenu(top, period, "Period","1min","5min", "30min", "1hr","3hr","12hr","24hr")
w.pack()


global NASAvar
NASAvar = tk.BooleanVar()
#NASAbox = tk.Checkbutton(top, text="NASA Photo of the Day",variable=NASAvar,justify=tk.LEFT,command=prnt)
NASAbox = filemenu.add_checkbutton(label="NASA Photo of the Day",  variable=NASAvar, command = prnt)
#NASAbox.pack()
global NASAlink
NASAlink = "http://apod.nasa.gov/apod/astropix.html"

global NATGEOvar
NATGEOvar = tk.BooleanVar()
#NATGEObox = tk.Checkbutton(top, text="NAT GEO Photo of the Day",variable=NATGEOvar,justify=tk.LEFT,command=prnt)
NATGEObox = filemenu.add_checkbutton(label="NAT GEO Photo of the Day",  variable=NATGEOvar, command = prnt)
#NATGEObox.pack()
global NATGEOlink
NATGEOlink = "http://photography.nationalgeographic.com/photography/photo-of-the-day/"

global VOLvar
VOLvar = tk.BooleanVar()
#VOLbox = tk.Checkbutton(top, text="Volcano Discovery Photo of the Day",variable=VOLvar,justify=tk.LEFT,command=prnt)
VOLbox = filemenu.add_checkbutton(label="Volcano Discover Photo of the Day",  variable=VOLvar, command = prnt)
#VOLbox.pack()
global VOLlink
VOLlink = "http://www.volcanodiscovery.com/photo-of-the-day.html"

top.mainloop()

