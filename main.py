import Webhook
import time
import os
import sys
import ctypes
import pymsgbox
from pathlib import Path

def find_initial_dir() -> str:

    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

    for drive in drives:
        drive_path = os.path.join(drive, '/Documents for Imaging/Clive/')
        if os.path.exists(os.path.abspath(drive_path)):
            return os.path.abspath(drive_path)
    
    return str(os.path.join(Path.home(), "Downloads"))

def run(select: int) -> int:
    """Function to run all Webhook class methods for the any source

    :param select: source selector
    :type select: int
    :return: total entries completed
    :rtype: int
    """

    if select > 3:
        raise ValueError('No Webhook repo associated with that number.')

    total = 0

    try:
        path = find_initial_dir()
        w = Webhook.Request(select, path)
        print(w.metadata)
        total = total + w.get_total()
        w.parse_metadata()

        return total
    except BaseException:
        ctypes.windll.user32.MessageBoxW(0, f"run() error encountered at ({select}). \n{sys.exc_info()}", "Warning!", 16)

if __name__ == "__main__":

    error_flag = 0
    time_cycles = 0
    upload_total = 0
    fee_total = 0

    value = pymsgbox.prompt('How many hours should the program run?', 'Input Dialog Box')

    if value == None or int(value) <= 0:
        raise ValueError("Input a time value of at least 1 or greater.")
    
    while(error_flag != 1 and time_cycles != int(value)):
        time_cycles += 1

        try:
            upload_total += run(1)
            fee_total += run(2)
        except BaseException as b:
            ctypes.windll.user32.MessageBoxW(0, f"__main__ error encountered at runtime. \n{sys.exc_info()[0]}, {sys.exc_info()[1]}", "Warning!", 16)
            error_flag = 1
        
        if int(value) != 1:
            time.sleep(3600)

    pymsgbox.alert(f"{upload_total+fee_total} documents pulled.\n{upload_total} upload and {fee_total} fee.", "Complete!")