# log file creating and exception file create 
'''
# 1 create log file

from us_visa.logger import logging
logging.info("Welcome to custom log")



from us_visa.exception import USvisaException
import sys
try:
    a =1/"10"
except Exception as e:
    logging.info(e)
    raise USvisaException(e, sys) from e
    
'''
# create artifact folder and data ingestion 
# from us_visa.constants import DATABASE_NAME

''' 
# 3 TO GET COLLECTION NAME we can use way to get



from us_visa.constants import*

print (COLLECTION_NAME)
'''

# run artifact, train test  data set by mongodb

from us_visa.pipline.training_pipeline import TrainPipeline


pipline  = TrainPipeline()
pipline.run_pipeline()
