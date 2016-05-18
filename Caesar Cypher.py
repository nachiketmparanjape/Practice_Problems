# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:51:54 2016

@author: Nachiket
"""

def caesar_cypher(offset,string):
    i = 0
    words = string.split()
    while i < len(words):
        word = words[i]
        j = 0
        while j < len(word):
            old_value = 0
            old_letter = word[j]
            old_value = ord(old_letter)
            
            new_value = old_value + offset
            if new_value > 122:
                new_value = new_value - 122 + 96
            word[j] = str(unichr(new_value))
            j += 1
        i += 1
    return words.join()