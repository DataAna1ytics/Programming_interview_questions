# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:23:54 2017

@author: Gavrilov
"""

grades = "5,5,5,5,5,4,5,5,4,5,4,5,5,5"
counter=0
summ=0
 
for item in grades:
    try:
        item==int(item)
    except ValueError:
        continue
    summ+=int(item)
    counter+=1

result=summ/counter
print(result)