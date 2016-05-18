# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 18:06:17 2016

@author: Nachiket
"""

#Check_Profanity
import urllib

def read_text():
    quotes = open("C:\Users\Nachiket\Google Drive\Python\Practice Problems\movie_quotes.txt")
    contents_of_file = quotes.read()
    print   contents_of_file
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    if 'true' in output:
        print 'Profanity Alert!'
    elif 'false' in output:
        print 'No curse word'
    else:
        print 'incorrect code'
    connection.close()
read_text()
    