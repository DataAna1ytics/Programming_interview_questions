# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:56:07 2017

@author: Gavrilov
"""
#In first string you have ID and lastname, and in second string you have full name.
#Write a code such that assignes ID to the full name

ID = "423754 Баженов \
429977 Барышев \
437058 Басаргин \
423612 Басулин \
431480 Бельянинов \
595586 Бирюков \
472711 Болахнин \
472687 Борукаев \
496650 Бочаров \
475532 Володин \
431601 Голендеева \
473016 Головацкий \
496920 Горяйнов \
473213 Заровнятных \
436758 Зубков \
424139 Иванов \
523772 Касьянов \
423597 Кац \
433185 Кириллов \
437088 Коновалов \
436925 Кудрин \
424334 Кузнецов \
428864 Курзенков \
430178 Литюк \
528644 Мантуров \
502779 Машевский \
423703 Нуртдинов \
435300 Плат \
528689 Пучков \
667563 Самолевский \
430106 Светельский \
596903 Сердюков \
436945 Сечин \
595550 Собянин \
431907 Субботин \
700825 Сурков \
594912 Текслер \
437081 Христенко \
431550 Чайка \
646377 Чижиков \
423798 Чинчуков \
437386 Шойгу \
423939 Шустов "

def List_ID_LastName(yourData): 
    List_ID = []
    counter_1 = 0
    counter_2 = 0
    for Element in ID:
        counter_1+=1
        if Element == " ":
            List_ID.append(ID[counter_2:counter_1])
            counter_2=counter_1
    return List_ID
List_ID = List_ID_LastName(ID)

def Dict_ID_LastName(List_ID):
     Dictionary_ID = {}
     counter = 0
     for Item in List_ID[::2]:
         counter+=2
         Dictionary_ID[Item] = List_ID[counter-1]
     return Dictionary_ID
Dictionary_ID = Dict_ID_LastName(List_ID)

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

def List_LastName_FirstName_MiddleName(yourData_2): 
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

def Reduced_List(Dictionary_ID, Name_2):
    Reduced_List = []
    for Element in Dictionary_ID.values():
        if Element in Name_2:
            Reduced_List.append(Element)
    return Reduced_List
Reduced_List=Reduced_List(Dictionary_ID, Name_2)

def Mach_ID(List_ID, Reduced_List):
    Mach_ID = {}
    counter = 0 
    for Item in List_ID:
        counter+=1
        if Item in Reduced_List:
            Mach_ID[List_ID[counter-2]] = Item
    return Mach_ID
Mach_ID = Mach_ID(List_ID, Reduced_List)

def Mach_ID_Full(Mach_ID, Name_2):
    Mach_ID_Full = Mach_ID.copy()
    y = 0
    for x in Mach_ID.keys():
        if Mach_ID[x] in Name_2:
            y = Name_2.index(Mach_ID[x])
            Mach_ID_Full[x]=Name_2[y:y+3]
    return Mach_ID_Full
Mach_ID_Full = Mach_ID_Full(Mach_ID, Name_2)
print("Dictionary of ID and Full name: ", Mach_ID_Full)
