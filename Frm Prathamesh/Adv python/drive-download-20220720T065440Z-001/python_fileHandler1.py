# import logging
# import python_fileHandler2
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
#
# file_handler = logging.FileHandler('sample.log')
# file_handler.setFormatter(formatter)
#
# logger.addHandler(file_handler)
#
# # logging.basicConfig(filename='sample.log',
# #                     level=logging.DEBUG,
# #                     format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')
#
#
# def addition(x, y):
#     return x + y
#
#
# def subtraction(x, y):
#     return x - y
#
#
# def multiplication(x, y):
#     return x + y
#
#
# def division(x, y):
#     return x / y
#
#
# a = 5
# b = 10
#
# addition_result = addition(a, b)
# logger.debug(f'The addition of {a} and {b} is {addition_result}')
#
# subtraction_result = subtraction(a, b)
# logger.debug(f'The subtraction of {a} and {b} is {subtraction_result}')
#
# multiplication_result = multiplication(a, b)
# logger.debug(f'The multiplication of {a} and {b} is {multiplication_result}')
#
# division_result = division(a, b)
# logger.debug(f'The division of {a} and {b} is {division_result}')

# ----------------------------------------------------------------------------------------------------------------------
# here we import file called python_fileHandler2 which configured with basicConfig() and set to level INFO. When we
# run python_fileHandler1 file which is also configured with basicConfig() having level DEBUG, it creates logs for only
# python_fileHandler2 because its level is higher and basicConfig() will called only once.

# for that we create separate logger for each file and provide handler to each logger.

# ----------------------------------------------------------------------------------------------------------------------

# if we set our logger to level info, but we want to only error messages inside sample.log file. To do that we set
# file_handler to that level.

# we can also add multiple handler

import logging
import python_fileHandler2

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# logging.basicConfig(filename='sample.log',
#                     level=logging.DEBUG,
#                     format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x + y


def division(x, y):
    try:
        result = x / y
    except Exception as e:
        logger.exception("Tried to divide by zero.")
    else:
        return result


a = 5
b = 0

addition_result = addition(a, b)
logger.debug(f'The addition of {a} and {b} is {addition_result}')

subtraction_result = subtraction(a, b)
logger.debug(f'The subtraction of {a} and {b} is {subtraction_result}')

multiplication_result = multiplication(a, b)
logger.debug(f'The multiplication of {a} and {b} is {multiplication_result}')

division_result = division(a, b)
logger.debug(f'The division of {a} and {b} is {division_result}')



