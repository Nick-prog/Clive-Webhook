import Webhook
import time
import os
import sys
from pathlib import Path
from typing import Tuple

def prompt_input(message: str) -> str:
    """Fallback prompt using stdin instead of pymsgbox (which may abort on older macOS)."""
    print(message)
    return input().strip()

def find_initial_dir() -> str:

    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

    for drive in drives:
        drive_path = os.path.join(drive, '/Documents for Imaging/Clive/')
        if os.path.exists(os.path.abspath(drive_path)):
            return os.path.abspath(drive_path)
    
    return str(os.path.join(Path.home(), "Downloads"))

def run(select: int) -> Tuple[int, int]:
    """Function to run all Webhook class methods for the any source

    :param select: source selector
    :type select: int
    :return: tuple of (events_processed, files_created)
    :rtype: Tuple[int, int]
    """

    if select > 3:
        raise ValueError('No Webhook source associated with that number.')

    events_processed = 0
    files_created = 0

    try:
        path = find_initial_dir()
        w = Webhook.Request(select, path)

        # Use the actual number of entries parsed (parse_metadata now returns count)
        processed = w.parse_metadata()
        events_processed = int(processed)

        x = Webhook.CSV(w.metadata, path)
        x.create_csv(select)

        # Count files created during this parse run
        files_created = w.count_files_created()

        return events_processed, files_created
    except BaseException:
        print(f"run() error encountered at ({select}). \n{sys.exc_info()}")
        return 0, 0

if __name__ == "__main__":
    try:
        error_flag = time_cycles = 0
        upload_events = upload_files = fee_events = fee_files = 0
        value = prompt_input('How many hours should the program run? (enter a number): ')

        if value == None or int(value) <= 0:
            raise ValueError("Input a time value of at least 1 or greater.")

        while(error_flag != 1 and time_cycles != int(value)):
            time_cycles += 1

            try:
                upload_evt, upload_fls = run(1)
                fee_evt, fee_fls = run(2)

                if upload_evt != 0:
                    upload_events += upload_evt
                    upload_files += upload_fls

                if fee_evt != 0:
                    fee_events += fee_evt
                    fee_files += fee_fls

            except BaseException:
                print(f"__main__ error encountered at runtime. \n{sys.exc_info()[0]}, {sys.exc_info()[1]}")
                error_flag = 1

            if int(value) != 1:
                time.sleep(3600)

        total_events = upload_events + fee_events
        total_files = upload_files + fee_files
        print(
            f"{total_events} events processed, {total_files} files created.\n"
            f"Upload: {upload_events} events, {upload_files} files\n"
            f"Fee: {fee_events} events, {fee_files} files"
        )
    except Exception as e:
        try:
            # prefer package logger if available
            from Webhook import logger as _logger
            _logger.logger.exception("Fatal error in main: %s", e)
        except Exception:
            import traceback
            traceback.print_exc()
        raise