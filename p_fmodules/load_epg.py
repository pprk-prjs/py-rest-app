'''
Created on Oct 10, 2017

@author: peperk
'''
import pytvinfo.pytvinfo.p_libs.p_utils as pu
import json
import traceback
import os
import time
import sys
import subprocess


def reload_epg():
#     print(os.getcwd())
    child = subprocess.Popen(["python3","./runner.py"], cwd=r'./pytvinfo/', shell=False)
    while True :
        if child.poll() is None:
            time.sleep(1)
        else:
            break
    
    return "FINISH" 
    

def _get_epg_file(today):
    if today:
        return pu.get_data_dir() + '/epg_td.json'
    else:
        return pu.get_data_dir() + '/epg_tm.json'


def _load_epg_file(_load_epg, today): 
    try:
        print("LOAD_EPG::", _load_epg)
        with open(_get_epg_file(today), 'r') as fp:
            return json.load(fp)
    except:
        if _load_epg:
            print('reloading epg ...')
            print(reload_epg()) 
            return _load_epg_file(False, today)
        else:
            print(traceback.format_exc())
        return {'ERR_MSG': "!!Reloading of EPG was not successful!!"}


def get_epg_all(_load_epg=True):
    dct = {}
    try:
        epg_str_td = _load_epg_file(_load_epg, True)
        epg_str_tm = _load_epg_file(_load_epg, False)
    except:
        print(traceback.format_exc())
        return {'ERR_MSG': "!!Reloading of EPG was not successful!!"}
    
    if 'ERR_MSG' in epg_str_td.keys(): 
        return epg_str_td['ERR_MSG']
    for tv_id in epg_str_td:
        try: 
#             print(">>>> ", tv_id)
            dct[tv_id] = [epg_str_td[tv_id], epg_str_tm[tv_id]]
        except KeyError as e:
            print(e, " >> ", tv_id)
            pass
    
    return dct

# reload_epg()
