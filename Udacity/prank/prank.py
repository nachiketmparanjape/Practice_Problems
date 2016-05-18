# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:43:14 2016

@author: Nachiket
"""
#r"C:\Users\Nachiket\Google Drive\Python\Practice Problems\Udacity\prank"
import os

def rename_files(link):
    #1. Get files from the folder
    file_list = os.listdir(link)
    print file_list
    
    #2. for each file, rename filename