# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 14:53:58 2016

@author: Nachiket
"""

#Factorial
def factorial(n):
    if n < 0:
        print "Please enter a positive integer"
    elif n == 0:
        factorial = 1
        return factorial
    else:
        factorial = 1
        while n > 0:
            factorial = factorial*n
            n -= 1
            return factorial