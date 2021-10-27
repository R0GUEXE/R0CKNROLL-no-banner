# r0ckNr0ll.py

import pyautogui
import time

def r0ck0n():
    txt = input("What would you like to spam?: ")

    dlay = input("How long do you want the delay before the spam to be? (default is 10 seconds): ")

    tmes = input("How many times do you want it to spam?: ")

    rdy = input("Are you ready to r0ck'N'r0ll? (y/m/q): ")

    if rdy == "y":
        print("r0ckin'N'r0lling!")
        if dlay == "":
            dlay = 10
        print(f"***(Make sure your cursor is in the right text input. YOU HAVE {dlay} SECONDS!)***")

    if rdy == "m":
        r0ck0n()

    if rdy == "q":
        print("Quitting!")
        time.sleep(3)
        quit()

    time.sleep(int(dlay))
    for i in range(int(tmes)):
        pyautogui.typewrite(txt)
        pyautogui.press("enter")


r0ck0n()
