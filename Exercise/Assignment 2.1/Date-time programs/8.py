# How to convert timestamp string to datetime object in Python?

import datetime
timestamp = datetime.datetime.fromtimestamp(1500000000)
print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))