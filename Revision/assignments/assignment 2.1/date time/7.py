# # time class: We can represent time values using the time class.
#
# import datetime
# abc = datetime.time(2, 24, 12, 5)
# print(abc)

# """Conversion from date to time: We can convert a date to its corresponding time
# using the strptime() function."""
#
# from datetime import datetime
# print(datetime.strptime("20/02/2023", "%d/%m/%Y"))


# time.strftime() in python: It converts a tuple or struct_time representing the time into a string object

from time import gmtime, strftime
s = strftime("%a, %d %b %Y %H:%M:%S + 10", gmtime())
print(s)
