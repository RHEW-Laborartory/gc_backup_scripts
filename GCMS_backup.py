#!/usr/bin/python
import datetime
import os


def date():
    """Uses datetime library to find todays date, and
    returns the string version."""
    today = datetime.dateime.now()
    return datetime.strftime("%y%m%d", today) 


def backup(date):
    """Python runs hidden shell prompt with the specified
    rsync command."""
    try:
        os.system("rsync -vaP /home/rob/halo1/ /media/rob/22C622FFC622D2B9/gcms_most_recent_backup")
    except Exception as e:
        print(e)


def main():
    try:
        os.system("cd /media/rob/22C622FFC622D2B9/ && mkdir gcms_most_recent_backup")
     except Exception:
        pass
    backup(date)


if __name__ == "__main__":
    main()
