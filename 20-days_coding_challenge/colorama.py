#!/usr/bin/python3
# craete a countdown timer

import colorama
from colorama import Fore
import time
import sys

def countdown(seconds):
    if seconds <= 0:
        print("seconds must be higher than {}".format(seconds))
    for remaining_seconds  in reversed(range(seconds)):
        #seconds -= 1
        mins, secs = divmod(remaining_seconds, 60)
        remaining_seconds = ("   {:02d}:{:02d}".format(mins, secs))
        time.sleep(1)
        print(remaining_seconds, end="\r")
    print("countdown of {} seconds completed". format(Fore.RED + seconds))
seconds = int(sys.argv[1])
countdown(seconds)