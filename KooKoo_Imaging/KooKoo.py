from tools import *
from sys import exit
import time
#***assigns letter to images partition if exists
usbIndex = getDiskpartDiskIndex("Removable Media")
if(usbIndex == None):
    Mbox("Could not find USB drive",0)
    exit()

#activate and assign the two USB partitions

cmd = "select disk " + usbIndex + """

select part 1
assign
select part 2
assign

"""
commandLine(cmd,"cmd.exe")
time.sleep(10)#give time to process commands

#Check for Winpe drive***
winPE = getUSBPart("WINPE")
if(winPE == None):
    Mbox("Could not find WINPE drive",0)
    exit()

#Check for Images Drive
images = getUSBPart("IMAGES")
if(images == None):
    Mbox("Could not find IMAGES drive",0)
    exit()

#run the main GUI





#create a backup function


#create a restore function