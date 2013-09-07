#!/usr/bin/env python

# example treeviewcolumn.py

#import pygtk as gtk
#pygtk.require('2.0')
import gtk
import webbrowser

class LinkTitle:
    
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def destroy(self, widget, data=None):
        print ""
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
        

def main():
    gtk.main()

if __name__ == "__main__":
    tvcexample = LinkTitle()
    main()
