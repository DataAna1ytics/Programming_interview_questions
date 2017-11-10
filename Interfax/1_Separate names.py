# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:01:44 2017

@author: Gavrilov
"""
#Separate first name, middle and last names from given text but keep order
Name_1 = "Басулин Александр Евгеньевич \
Текслер Алексей Леонидович \
Чайка Константин Леонтьевич \
Иванов Юрий Евгеньевич \
Чинчуков Юрий Леонидович \
Самолевский Сергей Витальевич \
Литюк Николай Петрович \
Светельский Владимир Николаевич \
Кац Александр Семенович \
Бирюков Алексей Сергеевич \
Шустов Николай Алексеевич \
Курзенков Геннадий Кузьмич \
Касьянов Александр Иванович \
Бельянинов Андрей Юрьевич \
Кузнецов Анатолий Владимирович \
Сурков Александр Владимирович \
Баженов Олег Валерьевич \
Барышев Павел Федорович \
Нуртдинов Ришат Васфиевич "

def List_LastName_FirstName_MiddleName(yourData): 
    Name_2 = []
    counter_1 = 0
    counter_2 = 0
    for Element in Name_1:
        counter_1+=1
        if Element == " ":
            Name_2.append(Name_1[counter_2:counter_1])
            counter_2=counter_1
    return Name_2
Name_2 = List_LastName_FirstName_MiddleName(Name_1)

def Dict_LastName_FirstName_MiddleName(Name_2):
    Dictionary = {}
    counter = 0
    for Item in Name_2[::3]:
        counter+=3
        Dictionary[Item] = [Name_2[counter-2], Name_2[counter-1]]
    return Dictionary
Dictionary = Dict_LastName_FirstName_MiddleName(Name_2)

def Print_LastName(Dictionary):
    print("Last names: ")
    for LastName in Dictionary.keys():
        print(LastName)
    return " "
print(Print_LastName(Dictionary))

def Print_FirstName(Dictionary):
    print("First names: ")
    for FirstName in Dictionary.values():
        print(FirstName[0])
    return " "
print(Print_FirstName(Dictionary))

def Print_MiddleName(Dictionary):
    print("Middle names: ")
    for MiddleName in Dictionary.values():
        print(MiddleName[1])
    return " "
print(Print_MiddleName(Dictionary))