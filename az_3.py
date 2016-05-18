# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:09:02 2016

@author: Nachiket
"""

def nearby_az(string):
    i1 = 0
    i2 = 0
    n = 0
    for i in string:
        if i == 'a':
            i1 = n
        n += 1
    n = 0
    for i in string:
        if i == 'z':
            i2 = n
        n += 1
    if i2-i1 > 0 & i2-i1 < 4:
        return True
    else:
        return False
            
            