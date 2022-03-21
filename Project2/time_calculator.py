# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:07:55 2022

@author: dejong71
"""
#______________________________________________________________________________

import Project2.helper_functions as hf

#______________________________________________________________________________

def add_time(start, duration, start_day=None):
    t1, t2 = map(hf.extract_hour_min, (start, duration))
    ttot = hf.sum_time(t1, t2)
    ttot = hf.find_period(ttot)
    day_msg = hf.format_days_passed_msg(ttot)
    curr_day_msg = hf.format_current_day_msg(start_day, ttot)

    return f'{ttot["hour"]}:{ttot["min"]:02} {ttot["period"]}{curr_day_msg}{day_msg}'

#______________________________________________________________________________