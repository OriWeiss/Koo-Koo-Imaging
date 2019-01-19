from tools import *
from sys import exit


if(int(getBuildNumber())< 15063): #checks to be sure creators update is installed
    Mbox("This Windows version is out of date. Please update to the newest windows to continue",0)
    exit()

Mbox('Please Insert USB > 10GB and remove all other devices then press OK', 0)

hddDrive = getHDD()
usb = getUSB()
winPE = ""
os = getOS()
cwd = getCWD()


#if usb is under sized
if(getPartSize(usb) < 10):
    Mbox("USB size is less than 10 GB please remove and reload KooKoo Imaging once corrected",0)
    exit()

usbIndex = getDiskpartDiskIndex("Removable Media")
cmd = 'select disk ' + usbIndex +r"""

clean
create partition primary size=600
format fs=fat32 quick  label="WINPE"
active
assign
create partition primary
format fs=NTFS quick label="IMAGES"
active
assign

"""
commandLine(cmd,"diskpart.exe")
time.sleep(10)#allow time for diskpart commands to process

#check if partitions were created
winPE = getUSBPart("WINPE")
if(winPE == None):
    Mbox("Could not find WINPE drive",0)
    exit()

if(getUSBPart("IMAGES") == None):
    Mbox("Could not find IMAGES drive",0)
    exit()

#copy windows pre installation environment files
copytree(cwd+r"\media",winPE)
Mbox("Finished creating USB", 0)