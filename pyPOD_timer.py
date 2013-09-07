def run_timer():
   import time
   import sys, time
   import shutil

   f = open('preferences.txt')
   lines = f.readlines()
   period = lines[0]
   f.close()
   sleeptime = 60
   if period == "1min\n":
      sleeptime = 60
   if period == "5min\n":
      sleeptime = 5*60
   if period == "30min\n":
      sleeptime = 30*60
   if period == "1hr\n":
      sleeptime = 60*60
   if period == "3hr\n":
      sleeptime = 3*60*60
   if period == "12hr\n":
      sleeptime = 12*60*60
   if period == "24hr\n":
      sleeptime = 24*60*60

   terminate = 0
   counter = -1
   numlinks = len(lines)- 1
   shortsleeptime = 2
   timeslept = 0
   continu = 1
   while terminate == 0:
      time.sleep(shortsleeptime)
      timeslept = timeslept + shortsleeptime
      f = open("refresh.txt")
      rr = f.readlines()
      f.close()
      f = open("stop.txt")
      ss = f.readlines()
      f.close()
      print timeslept
      if ss[0] == "1":
         terminate = 1
         continu = 0
      if rr[0] == "1":
         terminate = 1
         print "REFRESHED"
         f = open("refresh.txt","w")
         f.write("0")
         f.close
      if timeslept > sleeptime:
         timeslept = 0
         counter = counter + 1
         current_index = counter%numlinks + 1
         print lines[current_index]
         ci = open("currentimage.txt","w")
         ci.write(lines[current_index])
         ci.close()

   return continu

continu = 1
while continu == 1:
   continu = run_timer()
