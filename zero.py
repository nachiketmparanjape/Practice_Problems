# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:21:53 2016

@author: Nachiket
"""

def two_sum(nums):
    i1 = 0
    while i1 < len(nums):
        i2 = i1 + 1
        while i2 < len(nums):
            if nums[i1] + nums[i2] == 0:
                return [i1,i2]
            i2 += 1
        i1 += 1
    return []