import urllib

link = 'http://apod.nasa.gov/apod/image/1309/sgra_gasChandra_900c.jpg'
urllib.urlretrieve( link, 'img.jpg')


#from appscript import app, mactypes
#app('Finder').desktop_picture.set(mactypes.File('img.jpg'))

import subprocess

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def set_desktop_background(filename):
        subprocess.Popen(SCRIPT%filename, shell=True)

#set_desktop_background('img.jpg')
from appscript import app, mactypes
finder = app('Finder')
print finder
finder.desktop_picture.set(mactypes.File('img.png'))

