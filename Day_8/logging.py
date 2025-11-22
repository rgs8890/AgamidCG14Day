
'''
Logging -> This type of logging is essential
Catching Errors, Monitoring your performance, logging is a secret weapon
It is a way of recording all the messages that have been happening

Logs can only be saved to a file
Verify the code is executing as expected

Logging allows you to classify messages, info, warnings or errors

DEBUG
INFO
WARNING
ERROR
CRITICAL - Severe error that can end up 
'''

import logging
import mylib

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename = 'myapp.log', level = logging.INFO)
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')

# Setting up a logger involves
# Set up a logging configuration
logging.basicConfig(
    filename = log_file_name,
    level = logging.DEBUG,
    format = '%(asctime)s'
)
# Which level to show
# Add logs to your code

# When you need to review logs later, you can just do this via
# If one file causes an error, logging allows you to log all these
# Check the log to find out whihc file failed
# Why is it important for debugging monitoring or scaling programs?

'''
What is logging?
- Logging vs Print
- Logging Levels

'''