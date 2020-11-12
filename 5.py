# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:08:40 2020

@author: user
"""

print('Введите значение a')
a=int(input())
print('Введите значение b')
b=int(input())

# сложение, вычитание
adding=a+b
substraction=a-b
# умножение, деление
multiplication=a*b
division=a/b
# возведение в степень
scaling=a**b
# остаток от деления %
remainder=a%b
# деление до целого //
int_div=a//b
print('a+b',adding,'a-b',substraction,'a*b',multiplication,'a/b',division,'a^b',scaling,'a%b',remainder,'a//b',int_div)

x=3
y=5
z=7
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print(x==y)
print(x!=y)
print(y==z)
print(x>y and x<z)
print(y>x or y>z)
print(not(x>y))

bin(8)
oct(8)
oct(2)
oct(7)
round(1.4)
hex(16)
hex(15)
abs(-7.5)

x=13.5
y=13.1
z=13.986
rounding = round(z,2)
print(rounding)

round(5.5)
pow(3,3)

y=int(input('Enter number:'))
print(y+3)

num = input ("Enter number :") 
print(num) 
name1 = input("Enter name : ") 
print(name1) 

# power, % mod
b=pow(4,3,6)
print(b)

print (pow(3,4,10))

print (pow(3,-3,10))



# Найти гипотенузу треугольника
a=16; b=9; c=pow(pow(a,2)+pow(b,2),0.5); print(round(c,2))

print('Введите число')
a=int(input())
b=bin(a)
c=hex(a)
print('Двоичное',b,'Шестнадцатеричное',c)

for i in range(10): 
    print(i, end =" ") 


for i in range(3, 100, 25):
    print(i)
    
thislist = ["apple", "banana", "cherry"]
print(thislist)