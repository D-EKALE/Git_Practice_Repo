# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:11:25 2023

@author: Daniel Ekale
"""
import Maximum
import Minimum
def range_(problems):
    range_of_list = Maximum.max_number(problems) - Minimum.min_number(problems)
    print("The range of elements in our list is: ",range_of_list)
    return range_of_list

problems = [11,8,36,4,12,96,31,10,75,48,23,64,15,82]

range_(problems)