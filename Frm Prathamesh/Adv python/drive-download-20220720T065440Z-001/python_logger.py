# # Logging is a means of tracking events that happen when some software runs. The software’s developer adds logging
# # calls to their code to indicate that certain events have occurred.
#
# # With the logging module imported, you can use something called a “logger” to log messages that you want to see.
# # By default, there are 5 standard levels indicating the severity of events.
# # DEBUG : Detailed information, typically of interest only when diagnosing problem.
# # INFO : Confirmation that things are working as expected.
# # WARNING : Indication that something unexpected happened.
# # ERROR : Due to more serious issues some, software has not been able to perform some functions.
# # CRITICAL : A serious error, indicating that program itself may be unable to continue running.
#
# # Default level is warning, it means that only events with this level or above will be tracked.
#
# import logging
# logging.debug('Debug message')
# logging.info('Info message')
# logging.warning('Warning message')
# logging.error('Error message')
# logging.critical('Critical message')
#
# # The DEBUG and INFO message doesn't get printed this because default level is warning.
#
# # The output shows the severity level before each message along with root, which name given by logging module to its
# # default logger.

# ----------------------------------------------------------------------------------------------------------------------
# LOGGING TO A FILE
# ----------------------------------------------------------------------------------------------------------------------

# import logging
#
# logging.basicConfig(filename='logFile.log',
#                     filemode='w',
#                     level=logging.DEBUG,
#                     format='%(asctime)s : %(name)s : %(levelname)s : %(message)s'
#                     )
#
# logging.debug('Debug message.')
# logging.info('Info message.')
# logging.warning('Warning message.')
# logging.error('Error message.')
# logging.critical('Critical message.')
#
# # Some of commonly used parameters for the basicConfig()
# # level - root logger will set to specified severity level.
# # filename - This specifies the file
# # filemode - If filename is given, then file is opened in this mode. Default mode is append mode.
# # format - This is format of the log messages.

# ----------------------------------------------------------------------------------------------------------------------

# calling basicConfig() to configure root logger works only if the root logger has not been configured before.
# Basically, this function can only be called once.

# import logging
#
# logging.debug('Debug message.')
# logging.basicConfig(filename='logFile.log',
#                     filemode='w',
#                     level=logging.DEBUG,
#                     format='%(asctime)s : %(name)s : %(levelname)s : %(message)s'
#                     )
#
# logging.info('Info message.')
# logging.warning('Warning message.')
# logging.error('Error message.')
# logging.critical('Critical message.')

# debug(), info(), warning(), error() and critical() also called basicConfig() without argument if it has not been
# called before. This means that after the first time if one of the above function called then you can no longer
# configure the root logger because they would have called basicConfig() internally.

# ----------------------------------------------------------------------------------------------------------------------

# Exception information can be captured if the exc_info parameter is passed as True

# import logging
# logging.basicConfig(filename='logFile.log',
#                     filemode='a',
#                     level=logging.DEBUG,
#                     format='%(asctime)s : %(name)s : %(levelname)s : %(message)s'
#                     )
# a = 5
# b = 0
# try:
#     c = a / b
# except Exception as e:
#     logging.error('Exception occurred', exc_info=True)

# calling logging.error(exc_info=True) is same as calling logging.exception().

# import logging

# a = 5
# b = 0
# try:
#     c = a / b
# except Exception as e:
#     logging.exception('Exception occurred')

# ----------------------------------------------------------------------------------------------------------------------

