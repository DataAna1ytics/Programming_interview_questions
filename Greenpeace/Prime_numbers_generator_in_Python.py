# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:48:14 2017

@author: Gavrilov
"""
#Position: Senoir data analyst
#Task: Implement code to display prime numbers up to 100 in any programming language

lower = 2
upper = 101

def prime(x,y):
    result = []
    for num in range(lower,upper):
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            result.append(num)
    return(result)

print(prime(lower,upper))