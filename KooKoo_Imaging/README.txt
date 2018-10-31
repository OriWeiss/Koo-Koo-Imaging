PLEASE NOTE THAT AS OF 10/30/2018 ONLY PORTIONS OF THIS PROJECT ARE COMPLETED.
THE PROJECT WILL BE COMPLETED BY LATE JANUARY 2019 IF ANYONE IS INTERESTED IN WORKING ON THIS CODE PLEASE READ
DEVELOPERS SECTION


Welcome to KooKoo Imaging, your personal easy to use Windows imaging and restore tool.


Requirements:   1. A USB stick greater than or equal to 10 GB.
                2. A computer with Windows creators update (build number. 15063)


Instructions:
    Step 1. Run and follow all instructions in KooKoo_Create.py
    Step 2. Open bios and boot to USB device
    Step 3. WILL BE COMPLETED LATE JANUARY 2019


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
    Media directory
        Note: NOT completed.
        Purpose: To launch WinPe through bios


Legal
    No business or corporation shall be able to use or modify this code/program.

DEVELOPERS
    If you are interested in working and completing this code please email me at oriweiss212@gmail.com I will gladly
    help guide you through my ideas for how to complete KooKoo.py and run it in WinPe. I am currently taking a break
    on this project as school is keeping me busy.