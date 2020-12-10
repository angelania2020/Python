print(type(123))
#<class 'int'>


'Hello '+'world'
#'Hello world'

'Ang'+'elina'
#'Angelina'

10**3
#1000

10*3
#30

'Hi,'*10
#'Hi,Hi,Hi,Hi,Hi,Hi,Hi,Hi,Hi,Hi,'

'Hi'+2
#Traceback (most recent call last):
#  File "<pyshell#6>", line 1, in <module>
#    'Hi'+2
#TypeError: can only concatenate str (not "int") to str


int('56')
#56

int(3.14)
#3

int('word 56')
#Traceback (most recent call last):
#  File "<pyshell#9>", line 1, in <module>
#    int('word 56')
#ValueError: invalid literal for int() with base 10: 'word 56'

str(56)
#'56'

float('56')
#56.0

# Комментарий в одну строку
''' Несколько
        строчек
'''

'''Несколько
        строчек'''

"""Несколько
строчек"""

'''
Это строковый литерал.
Но здесь он используется как многострочный комментарий
'''

age=18
name='Name'
print(age)
print(name)

ä=3
print(ä)

ы=2
print(ы)

a=6
b=5
c=a+b
print(c)

print('Сумма:',c)

print('Сумма:', c)

print('Сумма:',a,'+',b,'=',c)
