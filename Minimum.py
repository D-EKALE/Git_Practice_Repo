# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:59:25 2023

@author: Daniel Ekale
"""
def min_number(problems):
    """A function to calculate the minimum number given a list of unsorted list"""
    lowest_number = problems[0]
    for number in problems:
        if number < lowest_number:
            lowest_number = number
    print(f"The lowest number is: {lowest_number}")
    return lowest_number
#A list to test
#problems = [11,8,36,4,12,96,31,10,75,48,23,64,15,82,30,77,15,1]

#call the function
#min_number(problems)