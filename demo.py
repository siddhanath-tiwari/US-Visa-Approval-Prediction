from us_visa.logger import logging
logging.info("Welcome to custom log")



from us_visa.exception import USvisaException
import sys
try:
    a =1/0 "10"
except Exception as e:
    raise USvisaException(e, sys) from e