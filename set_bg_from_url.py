import get_main_image as gmi
import os

# get the image
url = 'http://photography.nationalgeographic.com/photography/photo-of-the-day/'

gmi.get_main_image(url)
# the image is now current_image

# set it as the bg
os.system("osascript chdesk.scpt")

# change the fit pref
os.system("osascript setdeskfit.scpt")
