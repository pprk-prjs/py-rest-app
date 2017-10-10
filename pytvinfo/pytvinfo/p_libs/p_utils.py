'''
Created on Jan 6, 2017

@author: peperk
'''
from datetime import datetime
import time
import os

P_TIME_FORMAT = "%Y-%m-%d %H:%M:%S" 

def time_str(_datetime, tformat=P_TIME_FORMAT):
    return _datetime.strftime(tformat)

def str_time(_strtime, tformat=P_TIME_FORMAT):
    try:
        return datetime.strptime(_strtime, tformat)
    except TypeError:
        while True:
            try:
                return datetime(*(time.strptime(_strtime, format)[0:6]))
            except ImportError:
                time.sleep(0.1)
                
def get_data_dir():
    data_dir = lambda: os.environ.get('OPENSHIFT_DATA_DIR', os.path.expanduser('~/Downloads'))
    MY_DATA_DIR = data_dir() + '/DATA'
    if not os.path.isdir(MY_DATA_DIR):
        os.mkdir(MY_DATA_DIR)
    return MY_DATA_DIR
        
