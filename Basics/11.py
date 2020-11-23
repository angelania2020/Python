# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:09:05 2020

@author: user
"""

for i in range(1,11):
    print(f'Таблица умножения на {i}')
    for j in range(1,11):
        print(f'{i}x{j}={i*j}', end=' ')       
    print('')
    
for i in range(1,11):
    print(f'Таблица умножения на {i}')
    for j in range(1,11):
        print(f'{i}x{j}={i*j}') #Будет с новой строки
    print('')
        
#?'{0:>3}'
for i in range(1,11):
    for j in range(1,11):
        print('{0:>3}'.format(j*i), end=" ")
    print()
    
for i in range(1, 11):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j), end='') #\t - горизонтальная табуляция
        print()
        
for i in range(1, 11):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j))
        print()
    
    
    
import random

A=8
B=23

random.randint(A,B) #от 8 до 23

random.randrange(A,B,2) #шаг 2 и первое число

random.random()

a=random.randint(1,10)
print('a',a)

b=random.randrange(0,10,2)
print('b',b)

c=random.random()
print('c',c)

print('Введите количество куриц')
kurica=int(input())
print('Введите количество дней')
dni=int(input())
k=1.5
j=1.5
d=1.5
jaica=(j*kurica*dni)/(d*k)
#Только в этом задании можно сократить: jaica=(kurica*dni)/d
print(kurica,' куриц(ы) снесут', round(jaica), 'яиц за', dni, ' дней')


import random
numbers=random.randint(1,51)
c=True
while c:
    b=int(input('Введите целое число от 1 до 50: '))
    if b==numbers:
        print('Угадали')
        c=False
    elif 0<b<numbers:
        print('Загаданное компьютером число больше')
    elif 51>b>numbers:
        print('Загаданное компьютером число меньше')
    elif b<1 and b>50:
        b=int(input('Введите целое число от 1 до 50: '))
print('Цикл завершен')

a=list('lists')
print(a) #['l', 'i', 's', 't', 's']

Cars=['BMW','Opel','Ford','Porsche']
print(Cars)
print(Cars[3],'[3]')
for i in range(len(Cars)):
    print(Cars[i])
    
Cars=['BMW','Opel','Ford','Porsche']
for i in range(len(Cars)):
    print(Cars[i])
 
#Empty list. list.append adds elements in the end of the list
a=[]
n=int(input('How many elements will be in the list? '))
for i in range(n):
    e=int(input('Element: '))
    a.append(e)
print(a)

