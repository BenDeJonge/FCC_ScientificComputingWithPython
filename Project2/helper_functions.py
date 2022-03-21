# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:55:15 2022

@author: dejong71
"""

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

def extract_hour_min(timestamp : str) -> dict:
    '''
    Format a time in string format to a dictionary.

    Parameters
    ----------
    timestamp : str
        A timestamp in AM/PM format i.e., ``'hh:mm xM'``.

    Returns
    -------
    dict
        A timestamp as a dictionary of integers i.e. {'hour':hh, 'min':mm}.
    '''

    period = ''.join( char for char in timestamp if char.isalpha() )
    groups = ['','']
    i = 0
    for char in timestamp:
        if char.isnumeric():
            groups[i] += char
        else:
            i += 1
    h, m = (int(t) for t in groups)
    if period.upper() == 'PM':
        h += 12
    return {'hour'   : h,
            'min'    : m,
            'days'   : None,
            'period' : None}

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

def sum_time(t1 : dict, t2 : dict) -> dict:
    '''
    Add up two time dictionaries.

    Parameters
    ----------
    t1, t2 : dict
        Time dictionary {'hour' : h, 'min' : m}.

    Returns
    -------
    dict
        Time dictionary {'hour' : h, 'min' : m, 'days_passed' : d}.
    '''
    
    m = t1['min']  + t2['min']
    h = t1['hour'] + t2['hour'] + m // 60
    m %= 60
    days = h // 24
    h %= 24
        
    return {'hour'   : h,
            'min'    : m,
            'days'   : days,
            'period' : None}

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

def find_period(t : dict) -> dict:
    '''
    Fill the 'period' key of the time dict with 'AM' or 'PM'.

    Parameters
    ----------
    t : dict
        {'hour' : h, 'min' : m, 'days' : days, 'period' : None}.

    Returns
    -------
    dict
        {'hour' : h, 'min' : m, 'days' : days, 'period' : period}.
    '''
    period = 'AM'
    # 00:00 is 12:00 AM.
    if t['hour'] == 0:
        t['hour'] = 12
        period = 'AM'
    # 12:00 is 12:00 PM.
    elif t['hour'] == 12:
        period = 'PM'
    # 13:00 is 01:00 PM.
    elif t['hour'] > 12:
        t['hour'] -= 12
        period = 'PM'
    t['period'] = period
    return t

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

def format_days_passed_msg(t : dict) -> str:
    '''
    Output a formatted string indicating the number of days passed. Two forms
    are possible: ' (next day)' or ' ({n} days later)'.

    Parameters
    ----------
    t : dict
        {'hour' : h, 'min' : m, 'days' : days, 'period' : None}.

    Returns
    -------
    str
        A formatted string indicating the number of days passed.
    '''
    
    day_msg = ''
    if t['days'] == 1:
        day_msg = ' (next day)'
    elif t['days'] > 1:
        day_msg = f' ({t["days"]} days later)'
    return day_msg

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

def format_current_day_msg(start_day : str, t : dict) -> str:
    '''
    Output a formatted string indicating the full name of the current day.

    Parameters
    ----------
    start_day : str
        A string indicating the full name of the current day.
    t : dict
        {'hour' : h, 'min' : m, 'days' : days, 'period' : None}.

    Returns
    -------
    str
        'Monday', 'Tueday' etc.
    '''
    
    curr_day_msg = ''
    if isinstance(start_day, str):
        week = 'monday tuesday wednesday thursday friday saturday sunday'.split()
        i = week.index(start_day.lower())
        j = (t['days'] + i) % 7
        end_day = week[j]
        curr_day_msg = f', {end_day.capitalize()}'
    return curr_day_msg

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯