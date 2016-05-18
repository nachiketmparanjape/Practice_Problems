# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:04:43 2016

@author: Nachiket
"""

#Longest Word
def longest_word(sentense):
    words = sentense.split()
    lengths = []
    for word in words:
        lengths.append(len(word))
    x = lengths.index(max(lengths))
    return words[x]    
        