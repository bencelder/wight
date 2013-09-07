set screenMode to "Fit to Screen"
tell application "Finder"
          #set desktop picture to file "current_image" of (get path to desktop)
          set desktop picture to file "current_image" of (container of (path to me))
end tell

