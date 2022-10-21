# # Get Current Date and Time using Python

from datetime import datetime

current_dt = datetime.now()
print('now: ', current_dt)
dt_str = current_dt.strftime("%d/%m/%Y %H:%M:%S")
print("date and time: ", dt_str)
