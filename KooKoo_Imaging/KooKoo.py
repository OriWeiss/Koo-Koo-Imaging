from tools import *
from sys import exit

import shlex
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import subprocess
import time


#Check for Winpe drive***
winPE = getUSBPart("WINPE")
if(winPE == None):
    Mbox("Could not find WINPE drive",0)
    exit()
print("WinPe drive is",winPE)

#Check for Images Drive
images = getUSBPart("IMAGES")
if(images == None):
    Mbox("Could not find IMAGES drive",0)
    exit()
print("images drive is",images)

#check for Windows drive
hddDrive = getHDD()
if(hddDrive == None):
    Mbox("Could not find Windows drive",0)
    exit()
print("hdd drive is",hddDrive)



#create a backup/restore function


def run(command):
    progressBar['maximum'] = 100
    process = subprocess.Popen(shlex.split(command), stdin= subprocess.PIPE ,stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline().decode()
        if output == '' and process.poll() is not None:
            break
        if output:
            matchObj = re.search(r'\d+\.\d%',output.strip())
            if matchObj:
                percentNum = re.search(r'\d+\.\d',matchObj.group())
                progressBar["value"] = round(float(percentNum.__getitem__(0)))
                progressBar.update()
                print(progressBar["value"])

            else:
                progressBar.update()
                print(output.strip())

    rc = process.poll()
    progressBar["value"] = 0
    return rc

def restore():
    print("Running restore method")
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print("Reformatting Windows drive")
    format_drive(getHDD(), "NTFS", "Windows")
    time.sleep(10)
    restoreCmd = r'dism /Apply-Image /ImageFile:"' + filename.replace("/","\\") + r'" /Index:1 /ApplyDir:' + hddDrive
    print("Finished Formatting Windows drive")
    print("Running restore cmd")
    print("Restore command is " + restoreCmd)
    run(restoreCmd)

def backup(): #runs a gui to get a name for the file
    print("Running Backup method")
    main = tk.Tk()
    main.title("Choose File name")
    def my_function():
        fileName = my_entry.get()
        main.destroy()
        backupCmd = r'Dism /Capture-Image /ImageFile:'+images+'\\'+fileName+r'.wim /CaptureDir:' +hddDrive+ r' /name:Windows'
        print("Backup command is " + backupCmd)
        run(backupCmd)

    my_label = tk.Label(main, text="File Name ")
    my_label.grid(row=0, column=0)
    my_entry = tk.Entry(main)
    my_entry.grid(row=0, column=1)

    my_button = tk.Button(main, text="Submit", command=my_function)
    my_button.grid(row=1, column=1)

    main.mainloop()

#run the main GUI

root = Tk()
root.title('KooKoo Imaging')
root.geometry("300x100")

buttonFrame = LabelFrame(text="Options")
buttonFrame.grid(column=0,row=0)


button1 = Button(master=buttonFrame, text="Backup",command= lambda: backup())
button1.grid(column = 0, row = 0)


button2 =Button(master=buttonFrame, text="Restore",command= lambda: restore())
button2.grid(column = 50, row = 0)

button3 =Button(master=buttonFrame, text="Exit",command= lambda: exit())
button3.grid(column = 100, row = 0)

progressBar = ttk.Progressbar(root, orient="horizontal", length=286,mode="determinate")
progressBar.grid(column = 0, row = 3, pady=10)

root.mainloop()
