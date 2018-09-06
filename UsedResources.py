import os
import time
import win32
import psutil
from hurry.filesize import size

DriveLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Drives = ['%s:' % d for d in DriveLetters if os.path.exists('%s:' % d)]
DelayInSec = 60

def GetDriveUsage():
    for d in Drives:
        Usage = psutil.disk_usage(d)
        print(d)
        print("Used " + size(Usage[1]) + " | " + size(Usage[2]) + " free")

while True:
    lambda:os.system("cls")
    print("DRIVES" + "\n")
    GetDriveUsage()

    print("\nCPU" + "\n")
    print(str(psutil.cpu_percent()) + "%")

    VMemUsage = psutil.virtual_memory()
    print("\nRAM" + "\n")
    print(str(VMemUsage[2]) + "%")
    print("Used " + size(VMemUsage[3]) + " | " + size(VMemUsage[4]) + " free" + " | " + size(VMemUsage[0]) + " total")

    time.sleep(1)