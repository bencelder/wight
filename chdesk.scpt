#do shell script "/usr/bin/curl -o ~/Desktop/picture1.jpg http://apod.nasa.gov/apod/image/1309/sgra_gasChandra.jpg"
set screenMode to "Fit to Screen"
tell application "Finder"
          set desktop picture to file "picture1.jpg" of (get path to desktop)
end tell

