#note, pypiwin32 must be installed

import wmi
import os
from ctypes import *
import ctypes
import shutil
import subprocess

def getCWD(): #returns the CWD of the program
     return os.getcwd()

def getOS(): #returns the OS name
     c = wmi.WMI()
     for os in c.Win32_OperatingSystem():
          return os.Caption

def getUSB(): #returns the first USB drive letter found if no drive inserted returns NULL
     try:
          c = wmi.WMI()
          wql = "SELECT Caption FROM Win32_LogicalDisk WHERE DriveType <> 3"
          for disk in c.query(wql):
               diskLetter = disk.DeviceID
          return diskLetter
     except UnboundLocalError:
          return None

def getHDD(): #returns the hard drive disk letter. The hard drive should be named "Windows"
     c = wmi.WMI ()
     for physical_disk in c.Win32_DiskDrive ():
          for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"):
               for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"):
                    if ("Windows" == logical_disk.VolumeName):
                         return logical_disk.Caption

def getPartSize(driveLetter): #returns the size of the given partition
     c = wmi.WMI()
     for physical_disk in c.Win32_DiskDrive():
          for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
               for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                    if (driveLetter == logical_disk.DeviceID):
                         return (int(logical_disk.Size)/(1*(10**9))) #converts size to GB

def Mbox(text, style): #simple messagebox
    return ctypes.windll.user32.MessageBoxW(0, text, "KooKoo_Imaging", style)
    ##  Styles:
    ##  0 : OK
    ##  1 : OK | Cancel
    ##  2 : Abort | Retry | Ignore
    ##  3 : Yes | No | Cancel
    ##  4 : Yes | No
    ##  5 : Retry | No
    ##  6 : Cancel | Try Again | Continue

def copytree(src, dst, symlinks=False, ignore=None): #copies files in a specified directory to a destination
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def getUSBPart(volumeName): #returns the USB drive letter if no drive inserted returns NULL
    try:
        c = wmi.WMI()
        wql = "SELECT VolumeName FROM Win32_LogicalDisk WHERE DriveType <> 3"
        for disk in c.query(wql):
            if(volumeName == disk.VolumeName):
                diskLetter = disk.DeviceID
                return diskLetter
        return None
    except UnboundLocalError:
        return None

def getBuildNumber(): #returns the os version or build number
    c = wmi.WMI()
    for os in c.Win32_OperatingSystem():
        return os.BuildNumber

def getDiskpartDiskIndex(mediaType): #returns the disk index in form of string, can be used for diskpart commands
    c = wmi.WMI()
    for physical_disk in c.Win32_DiskDrive():
        if(mediaType == physical_disk.MediaType):
            return str(physical_disk.Index)
    #can be either Removable Media or Fixed hard disk media

def getDiskpartPartitionIndex(volumeName): #returns the partition index in form of string, can be used for diskpart commands
    c = wmi.WMI()
    for physical_disk in c.Win32_DiskDrive():
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                if(volumeName == logical_disk.VolumeName):
                    return str(partition.Index)

def commandLine(commands,program): #input multiple commands in form of block string, outputs stdout and stderr
    process = subprocess.Popen(program, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = process.communicate(bytes(commands,'utf-8'))
    return out,err

#this code can be used to see all the data WMI provides
""" 
c = wmi.WMI()
for physical_disk in c.Win32_DiskDrive():
    for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
        for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
            print (physical_disk,partition,logical_disk)
"""