# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:32:11 2016

@author: Nachiket
"""
#min to hh:mm
def time_conversion(minutes):
    hh = minutes/60
    mm = minutes%60
    if mm<10:
        mm = str(0)+str(mm)
    else:
        mm = str(mm)
    if hh<10:
        hh = str(0)+str(hh)
    else:
        hh = str(hh)
    hhmm = hh+':'+mm
    return hhmm