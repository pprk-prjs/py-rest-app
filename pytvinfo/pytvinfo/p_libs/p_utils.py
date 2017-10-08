'''
Created on Jan 6, 2017

@author: peperk
'''
from datetime import datetime
import time
import traceback
# import xbmc
# import xbmc

P_TIME_FORMAT = "%Y-%m-%d %H:%M:%S" 

def time_str(_datetime, format=P_TIME_FORMAT):
    return _datetime.strftime(format)

def str_time(_strtime, format=P_TIME_FORMAT):
    try:
        return datetime.strptime(_strtime, format)
    except TypeError:
        while True:
            try:
                return datetime(*(time.strptime(_strtime, format)[0:6]))
            except ImportError:
                time.sleep(0.1)
        
def try_except(exc_type):
    def _try_except(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exc_type as e:
                _print_exception(e)
        
        return inner
    return _try_except
                
def _print_exception(exc, msg=""):
    _print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!","!")
    exc = traceback.format_exc()
    _print(exc, "!!! EXCEPTION::: " + msg + "\n")
    _print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!","!")
    
def _print(val, prefix = ">>>>>> "):
    xbmc.log("=== DEF_SCR === " + prefix + str(val))
        
