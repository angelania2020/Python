# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:31:21 2020

@author: user
"""

tovar1=50
tovar2=32
if tovar1+tovar2>99:
    print ('Сумма недостаточна')
else:
    print ('Чек оплачен')
    
#
x=-10
if x>0:
    print (1)
elif x<0:
    print(-1)
else:
    print(0)
    
    
a=int(input())
b=int(input())
if a>b:
    c=a-b
elif a<b:
    c=a+b
else:
    c=a
print(c)
    

a=int(input())
if a<-5:
    print('Low')
elif -5<=a<=5:
    print('Mid')
else:
    print('High')
    
    
result = 'no result'
num1 = int(input())
if num1 == 0:
    result = 0
elif num1==1:
    result = 1
elif num1==2:
    result = 2
elif num1==3:
    result=3
elif num1==4:
    result=4
elif num1==5:
    result=5
else:
    print ('Error')
print(result)


str1 = '+'
i = 0
while i < 10:
    print (str1)
    i = i + 1
    
#fib1, fib2 только 1 раз напишет, а сумму по циклу
fib1=0
fib2=1
print(fib1)
print(fib2)
n=10
i=0
while i<n:
    fib_sum = fib1 + fib2
    print(fib_sum)
    fib1=fib2
    fib2=fib_sum
    i=i+1
    
    

for i in range(1,11):
    print(i)
    
for i in range(0,10):
    print(i)
    
    
for i in range(1,11):
    for j in range (1,11):
        print('* ', end='')
    print ()

    
    
# 11 индексов, обращение по индексу, но первая буква - 0
t = 'Hello world'
print(t[10])
print(t[2:5])
print(t[:4])
print(len(t))
print(t[len(t)-1])
print(t[len(t)-2])


tekst = 'Hello World'
print(tekst.capitalize())
print(tekst.upper())
print(tekst.lower())
print(tekst.swapcase())