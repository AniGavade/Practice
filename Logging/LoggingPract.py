# DEBUG: Details information, typically of interest only when diagnosing problems.

# INFO: confirmation that things are working as expected.

# WARNING: An indication that somthing unexpected happened, or indicative of some problem in the near future (e.g. "disk space low"). The software still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

from __future__ import division


def add(x, y):
    """Add function"""
    return x + y

def substract(x, y):
    """Substract function"""
    return x + y

def multiply(x, y):
    """multiply function"""
    return x + y

def divide(x, y):
    """devide function"""
    return x + y

num_1 = 15
num_2 = 10

add_result = add(num_1, num_2)
print("Add: {} + {} = {}".format(num_1, num_2, add_result))

sub_result = substract(num_1, num_2)
print("Sub: {} - {} = {}".format(num_1, num_2, sub_result))

mult_result = multiply(num_1, num_2)
print("Mult: {} * {} = {}".format(num_1, num_2, mult_result))

div_result = divide(num_1, num_2)
print("Div: {} / {} = {}".format(num_1, num_2, div_result))

pass




# import logging
# logging.basicConfig(filename="log1.log",level=logging.DEBUG,format='%(asctime)s %(message)s')
# # logger=logging.getLogger()
# # logger.setLevel(logging.DEBUG)

# str = 'www.google.com'
# logging.debug("Google is search engine")
