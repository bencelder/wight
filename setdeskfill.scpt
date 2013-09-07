set screenMode to item 2 of {"Fill Screen", "Fit to Screen", "Center"}
set frequency to item 3 of {"Every 5 seconds", "Every minute", "Every 5 minutes", "Every 15 minutes", "Every 30 minutes", "Every hour"}
 
tell application "System Preferences"
    -- activate
    reveal anchor "DesktopPref" of pane id "com.apple.preference.desktopscreeneffect"
    repeat until window "Desktop & Screen Saver" exists
        delay 0.1
    end repeat
   
    tell application "System Events" to tell window "Desktop & Screen Saver" of process "System Preferences"
        tell tab group 1
            click pop up button 2
            click menu item screenMode of menu 1 of pop up button 2
        end tell
    end tell
    quit
end tell
