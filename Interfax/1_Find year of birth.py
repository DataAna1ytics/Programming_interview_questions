# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:06:47 2017

@author: Gavrilov
"""
#Position of an Analyst
#Find year of birth in given biography
Bio = "Родился 14 сентября 1965 года в Ленинграде. \
Окончил юридический факультет Ленинградского государственного университета в 1987 году \
и аспирантуру ЛГУ в 1990 году. Кандидат юридических наук, доцент \
В 1990 — 1999 годах — на преподавательской работе в Санкт-Петербургском государственном университете. \
Одновременно в 1990 — 1995 годах — советник Председателя Ленинградского городского совета, \
эксперт Комитета по внешним связям Мэрии Санкт-Петербурга."

def FirstTry(Bio, counter):
    result = ""
    while True:
        for Element in Bio:
            counter+=1
            if Element in "0123456789":
                result+=Element
                if len(result) == 4:
                    break
            elif Bio[counter] == " ":
                result= ""
            else:
                continue
        return [result, counter]
counter = -1
result_1 = FirstTry(Bio, counter)

def SecondTry(result_1, Bio):
    counter = result_1[1]
    result=""
    while True:
        for Element in Bio[counter:]:
            counter+=1
            if Element in "0123456789":
                result+=Element
                if len(result) == 4:
                    break
            elif Bio[counter] == " ":
                result= ""
            else:
                continue
        return [result, counter]
result_2 = SecondTry(result_1, Bio)

def DataToCompare_1(result_1, result_2):
    if result_1[0] < result_2[0]:
        return result_1
    else:
        return result_2
Compare_1 = DataToCompare_1(result_1, result_2)
print("Year of birth is: ", int(Compare_1[0]))
