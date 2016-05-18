# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:09:55 2016

@author: Nachiket
"""
import turtle

def square(some_turtle):
    
    some_turtle.color("red")
    some_turtle.shape("turtle")
    i = 0
    while i < 5:
        some_turtle.forward(100)
        some_turtle.right(90)
        i += 1
        
def art():
    mark = turtle.Turtle()
    j = 0
    while j < 16:
        square(mark)
        mark.right(24)
    mark.onclick(exit)


art()