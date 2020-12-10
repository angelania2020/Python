# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:38:04 2020

@author: user
"""
# Пользователь вводит радиус, программа отображает площадь круга
print('Введите радиус r:')
r=int(input())
S=3.14*r**2
print(S)

#Пользователь вводит длины a и b прямоугольника, программа отображает площадь и периметр
print('Print a')
a=int(input())
print('Print b')
b=int(input())
S=a*b
P=2*(a+b)
print('S =',S,'P =',P)

#Пользователь вводит номер дня недели, программа отображает название дня недели

#Не доделали
print('Введите номер дня недели:')
n=int(input())
if 0<n<=7:
    for i in range(1,7):

#Не доделали
print('Введите номер дня недели:'))    
n=int(input())
day={'пн':1,'вт':2,'ср':3,'чт':4,'пт':5,'сб':6,'вс':7}
print('n', n)

#Maria
day=int(input('Print the day of the week:'))
if day==1:
    print('Monday')
else:
    if day==2:
        print('Tuesday')
    else:
        if day==3:
            print('Wednesday')
        else:
            if day==4:
                print('Thursday')
            else:
                if day==5:
                    print('Friday')
                else:
                    if day==6:
                        print('Saturday')
                    else:
                        if day==7:
                            print('Sunday')
                        else:
                            print('Invalid number of the day of the week!')
                        
#Egor
print('Insert number of day')
n=int(input())
i=0
if 0<n<=7:
    while i!=1:
       if n==1:
           print('Monday')
           i=1
       if n==2:
           print('Tuesday')
           i=1
       if n==3:
           print('Wednesday')
           i=1
       if n==4:
           print('Thursday')
           i=1
       if n==5:
           print('Friday')
           i=1
       if n==6:
           print('Saturday')
           i=1
       if n==7:
           print('Sunday')
           i=1
else:
    print('Invalid number')
    
#Internet
weekday = int(input("Enter weekday day number (1-7) : "))

if weekday == 1 :
    print("\nMonday");

elif weekday == 2 :
    print("\nTuesday")

elif(weekday == 3) :
    print("\nWednesday")

elif(weekday == 4) :
    print("\nThursday")

elif(weekday == 5) :
    print("\nFriday")

elif(weekday == 6) :
    print("\nSaturday")

elif (weekday == 7) :
    print("\nSunday")

else :
    print("\nPlease enter weekday number between 1-7.")
    
#Пользователь вводит номер месяца, программа отображает название месяца

month = int(input('Enter month number (1-12) : '))

if month == 1 :
    print('\nJanuary')

elif month == 2 :
    print('\nFebruary')

elif month == 3 :
    print('\nMarch')

elif month == 4 :
    print('\nApril')

elif month == 5 :
    print('\nMay')

elif month == 6 :
    print('\nJune')

elif month == 7 :
    print('\nJuly')

elif month == 8 :
    print('\nAugust')

elif month == 9 :
    print('\nSeptember')

elif month == 10 :
    print('\nOctober')

elif month == 11 :
    print('\nNovember')

elif month == 12 :
    print('\nDecember')

else :
    print('\nPlease enter month number between 1-12.')
    
    
print('Введите значение x')
x=int(input())
if x>0:
    y=2*x
else:
    y=-2*x
print(y)
