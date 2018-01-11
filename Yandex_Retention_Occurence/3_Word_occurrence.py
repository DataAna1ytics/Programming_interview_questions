# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:59:01 2017

@author: Gavrilov
"""
#Position: Analyst for Yandex vertical services (auto.ru, realty.yandex.ru, rabota.yandex.ru, travel.yandex.ru)
#Task: Implement code which counts occurrence of a word in a string using specific Python function    
#On-site interview

s = 'qwert, tyuio, yuio, sdfg, qwert, fghjk, '
import collections
c = collections.Counter()
x=s.split(', ')
for word in x:
    c[word]+=1
print(c)
