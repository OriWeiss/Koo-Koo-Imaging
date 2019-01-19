Welcome to KooKoo Imaging, your personal easy to use Windows imaging and restore tool.


Requirements:   1. A USB stick greater than or equal to 10 GB.
                2. A computer with Windows creators update (build number. 15063)


Instructions:
    Step 1. Download KooKoo folder from https://drive.google.com/file/d/19SiByyWmaDnlMqICGN4A7LgMVzVfCB98/view?usp=sharing
    Step 2. Run and follow all instructions in KooKoo_Create.py
    Step 3. Open bios and boot to USB device (Particluarly the WinPE partition)
    Step 4. Type diskpart and press enter
    Step 5. Find and note the drive letter of the WinPe partition
    step 6. Type exit and press enter.
    Step 7. Run the KooKoo Imaging program by doing the following:
	I. type "Your Drive Letter":\Python37-amd64\python.exe "Your Drive Letter":\KooKoo\KooKoo.py
		For example if your WinPe drive was labeled 'F' your command would be
		F:\Python37-amd64\python.exe F:\KooKoo\KooKoo.py

	Note: All Images backed up will be placed onto the "Images" partition of the USB Drive

Files
    This tool is broken down into three files, tools.py, KooKoo.py, and KooKoo_Create.py

    tools.py
        Purpose: This a file of functions that will be used in KooKoo.py and KooKoo_Create.py

    KooKoo_Create.py
        Requirements:This file requires a USB of size 10 GB or greater to be placed into the computer.
        Purpose: To properly partition and format a USB drive that will carry the KooKoo program. The USB will run
            the windows pre installation environment along with the KooKoo tool. This file also copies the media directory
            (contains all needed files to boot WinPE) to the USB The windows pre installation environment
            should be booted up through the WINPE partition created on the USB. The Images Partition is used to store
            captured .wim files.
    KooKoo.py
        NOTE: This portion of the code is uncompleted and will be finished and uploaded by late January 2019
        Purpose: This is the main program that will run in windows pre installation environment. It will be able
            to backup and restore a chosen image. Since python files can not be run on windows pre installation
            environment a tool will be used to convert to an executable
    KooKoo_Files directory
        Note: The WMI Package is installed to WinPE
	Note:Python 64 bit and the WMI package are installed
	Purpose: To launch WinPe through bios which allows the launch of KooKoo Imaging though Python 3.7amd64
	


Legal
    No business or corporation shall be able to use or modify this code/program.