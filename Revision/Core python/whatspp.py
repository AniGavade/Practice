# import pywhatkit
#
# pywhatkit.sendwhatmsg('+91 82755 19438', 'Chal re laundry che kapde anu.', 15, 32)
#

import pyautogui as pt
import time

limit_ = input("Enter limit: ")
message_ = input("Enter message: ")
i = 0

time.sleep(3)

while i < int(limit_):
    pt.typewrite(message_)
    pt.press("enter")

    i += 1
