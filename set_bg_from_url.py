import get_main_image as gmi
import os
import sys

def set_bg(url):
    #url = 'http://photography.nationalgeographic.com/photography/photo-of-the-day/'
    print url

    # get the image
    gmi.get_main_image(url)
    # the image is now current_image

    # set it as the bg
    os.system("osascript chdesk.scpt")

    # change the fit pref
    os.system("osascript setdeskfit.scpt")

if __name__ == "__main__" :
    set_bg(sys.argv[1])
