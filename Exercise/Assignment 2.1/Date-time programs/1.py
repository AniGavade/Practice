# # Python program to get Current Time.
# # 1) Getting current time using time module.

# import time
#
# time_obj = time.localtime()
# current_time = time.strftime("%H:%M:%S", time_obj)      #returning a string representing date and time using a date, time, or datetime object
# print("Current time is: ", current_time)
# ______________________________________________________________________________________________________________________

# 2) getting current time using datetime object

# from datetime import datetime
#
# obj_now = datetime.now()
# current_time = obj_now.strftime("%H:%M:%S")
# print("Current time is: ", current_time)
# ______________________________________________________________________________________________________________________
