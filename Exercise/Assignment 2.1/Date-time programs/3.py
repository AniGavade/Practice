# # Find yesterday’s, today’s and tomorrow’s date

import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
print('Yesterday : ', yesterday)

