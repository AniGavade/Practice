# DEBUG: Details information, typically of interest only when diagnosing problems.

# INFO: confirmation that things are working as expected.

# WARNING: An indication that somthing unexpected happened, or indicative of some problem in the near future (e.g. "disk space low"). The software still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# from __future__ import division


# def add(x, y):
#     """Add function"""
#     return x + y

# def substract(x, y):
#     """Substract function"""
#     return x + y

# def multiply(x, y):
#     """multiply function"""
#     return x + y

# def divide(x, y):
#     """devide function"""
#     return x + y

# num_1 = 15
# num_2 = 10

# add_result = add(num_1, num_2)
# print("Add: {} + {} = {}".format(num_1, num_2, add_result))

# sub_result = substract(num_1, num_2)
# print("Sub: {} - {} = {}".format(num_1, num_2, sub_result))

# mult_result = multiply(num_1, num_2)
# print("Mult: {} * {} = {}".format(num_1, num_2, mult_result))

# div_result = divide(num_1, num_2)
# print("Div: {} / {} = {}".format(num_1, num_2, div_result))

# pass


# import logging
# logging.basicConfig(filename="log1.log",level=logging.DEBUG,format='%(asctime)s %(message)s')
# # logger=logging.getLogger()
# # logger.setLevel(logging.DEBUG)

# str = 'www.google.com'
# logging.debug("Google is search engine")


# import threading
# import time
# def rohit(age):
#     print("thread started",age)
#     time.sleep(4)
#     print('hello sleeping for 2')
#     time.sleep(4)
#     print("something happened")

# for i in range(5):
#     # obj = rohit(i)
#     t = threading.Thread(target = rohit,args=(i,))
#     t.start()
#============================================
# import logging
# #create logger
# logger = logging.getLogger("simple prob")
# #setting level of logger
# logger.setLevel(logging.DEBUG)

# #create console handler
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)

# #create a formatter

# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# #add formatter to console handler

# console_handler.setFormatter(formatter)

# #add handler to logger

# logger.addHandler(console_handler)

# #application code

# logger.debug("im debugging")
# logger.info("im informimg")
# logger.warning("im warning you")
# logger.error("im throwing errror")
# logger.critical("im too critical to handle")
#===================================
# import logging
# #create logger
# logger = logging.getLogger("simple prob")
# #setting level of logger
# logger.setLevel(logging.DEBUG)

# #create console handler
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)

# #create a formatter

# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# #add formatter to console handler

# console_handler.setFormatter(formatter)

# #add handler to logger

# logger.addHandler(console_handler)

# #application code
# logger.removeHandler(console_handler) #what happens if you remove handler???

# logger.debug("im debugging")
# logger.info("im informimg")
# logger.warning("im warning you")
# logger.error("im throwing errror")
# logger.critical("im too critical to handle")

# import logging
# import logging.config

# logging.config.fileConfig('logging.conf')

# # create logger
# logger = logging.getLogger('simpleExample')

# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

# import logging 

# logging.basicConfig(filename='rohit.txt',encoding='utf-8',level=logging.DEBUG)

# logging.debug("hello im debuging")
# logging.critical("im critical")

import threading

import time

def ani(sec):
    print("before slepping",sec)
    print()
    time.sleep(sec)
    print("im done sleeping",sec)

for i in range(5,-1,-1):

    t = threading.Thread(target=ani,args =(i,))
    t.start()
    t.join()
    print("Hello")