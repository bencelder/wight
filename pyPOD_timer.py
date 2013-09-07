import time
import sys, time, msvcrt
import shutil

f = open('preferences.txt')
lines = f.readlines()
period = lines[0]
f.close()
if period == "1min":
   sleeptime = 60
if period == "5min":
   sleeptime = 5*60
if period == "30min":
   sleeptime = 30*60
if period == "1hr":
   sleeptime = 60*60
if period == "3hr":
   sleeptime = 3*60*60
if period == "12hr":
   sleeptime = 12*60*60
if period == "24hr":
   sleeptime = 24*60*60

terminate = 0
counter = -1
numlinks = len(lines)- 1
sleeptime = 3
print sleeptime
while terminate == 0:
   counter = counter + 1
   current_index = counter%numlinks + 1
   time.sleep(sleeptime)
   print lines[current_index]

