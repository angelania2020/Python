# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:20:30 2020

@author: user
"""

tekst='       Hello World      '
print(len(tekst))
print(tekst.strip())
print(tekst.rstrip())
print(tekst.lstrip())

t='Hello World'
print(t.strip('dH'))
print(t.strip('Hd'))

t='llo Worl'
print(t.strip('l'))

t1 = 'Hello World'
print(t1.count('l'))      #3
print(t1.find('World'))   #index 6
print(t1.find('x'))       #-1
print(t1.index('x'))      #ValueError 

tekst='Hello World'
print(tekst.isalnum())
print(tekst.isalpha())
print(tekst.isdigit())
print(tekst.isupper())
print(tekst.islower())
print(tekst.endswith('d'))
print(tekst.startswith('H'))

print('ü' in tekst)
print('@' not in tekst)

print(tekst.replace('l','p'))

tekst= 'Hello Big Happy World'
numbers = '1;2;3;4'
print(tekst.split( ))
print(numbers.split(';'))

print(':'.join(['hello','big','happy','world']))

times = '14:38'
hours, minutes = times.split(':')
print(hours, minutes)

name='Nikita'
print(f"Привет,{name}")

name="Nikita"
print(f"Привет,{name}")

print('Введите своё имя')
name=input()
print(f'Привет, {name.upper()}!')

print('Введите своё имя')
name=input()
a,b = 5,2
print(f'Привет, {name}! {a}+{b}={a+b}?')

print('в одну "строку"')
print('''в
несколько
"строк"''')
      
print(f'{2 * 2}')






