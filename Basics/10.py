# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:15:47 2020

@author: user
"""

print('Введите количество куриц')
kurica=int(input())
print('Введите количество дней')
dni=int(input())
k=1.5
j=1.5
d=1.5
jaica=kurica*(dni/d)
print(kurica,' куриц(ы) снесут', jaica, 'яиц за', dni, ' дней')


print('Введите возраст брата')
brat2=int(input())
sestra=3
brat=3*2
raznica=brat-sestra
sestra2=brat2-raznica
print('Возраст сестры будет:', sestra2, 'лет/года')


i=1 #счётчик
for color in 'red','orange','yellow','green','cyan','blue','violet':
    print('#',i,color,sep=' ')
    i=i+1

for i in 1,2,3,'one','two','three':
    print(i)
    
for color in 'red','orange','yellow','green','cyan','blue','violet':
    print(color)

for i in range(4):
    print(i)
    print(i**2)
print('end')

for i in range(4):#0,1,2,3
    print('#i',i)
    print('i**2',i**2)
print('end')


sum=0
n=5
for i in range(1, n+1): #ДО 6
    sum += i
print(sum)

sum=0
n=5
for i in range(1, n+1):
    sum = sum+i
print(sum)

print(1,2,3)
print(4,5,6)
print(1,2,3, sep=', ', end='. ')
print(4,5,6, sep=', ', end='. ')
print()
print(1,2,3, sep='', end=' -- ')
print(4,5,6, sep=' * ', end='.')


                   
i = 1
while i < 101:
    if i%5==0:
        print(i)
    i += 1
     
for city in 'Narva','Rakvere','Tallinn':
    print(city)

i=1
for city in 'Narva','Rakvere','Tallinn':
    print(i, city)
    i=i+1
print()

#FizzBuzz
for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else: print(i)
        
sum=0
for i in 10,12,13,20,5,8:
    sum=sum+i
    print(i)
print(sum)

row=int(input('Введите количество строк: '))
col=int(input('Введите количество столбцов: '))
for i in range(row):
    for j in range (col):
        print('* ', end='')
    print () #пустая строчка