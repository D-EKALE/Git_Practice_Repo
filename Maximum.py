# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:49:59 2023

@author: Daniel Ekale
"""

def max_number(problems):
    """A function to calculate the maximum number given a list of unsorted list"""
    highest_number = problems[0]
    for number in problems:
        if number > highest_number:
            highest_number = number
    print(f"The highest number is: {highest_number}")
    return highest_number
#A list to test
#problems = [1,8,36,4,12,96,31,10,75,48,23,64,15,82,30,77,15]

#call the function
#max_number(problems)

