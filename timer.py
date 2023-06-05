"""
@author: amro almaghraba
Release: 21 MAY 2023
@version: V1.0
This project to minimize all windows after specific time 
"""
import time
import winsound
import pyautogui

tim = 20 #time in minute
tis = tim * 60 #converter time to seconds

for x in range (1, 4, 1):
   time.sleep(tis) 
   pyautogui.hotkey('win', 'm')
   duration = 1000
   freq =440
   winsound.Beep(freq, duration)
   print('continue?')
   x = input()
   if x=="n":
      break;
   
if x=="n":
   print("done")
else:
   for x in range (1,5,1):
      duration = 500
      freq =440
      winsound.Beep(freq, duration)
      time.sleep(0.25)
