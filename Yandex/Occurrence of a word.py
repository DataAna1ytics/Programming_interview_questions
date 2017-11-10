# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:59:01 2017

@author: Gavrilov
"""
#Analyst position for Yandex vertical services

#write code which counts occurrence of a word in a "s"
s = 'qwert, tyuio, yuio, sdfg, qwert, fghjk, '
import collections
c = collections.Counter()
x=s.split(', ')
for word in x:
    c[word]+=1
print(c)