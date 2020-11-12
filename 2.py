Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(type(123))
<class 'int'>
>>> 'Hello '+'world'
'Hello world'
>>> 'Ang'+'elina'
'Angelina'
>>> 10**3
1000
>>> 10*3
30
>>> 'Hi,'*10
'Hi,Hi,Hi,Hi,Hi,Hi,Hi,Hi,Hi,Hi,'
>>> 'Hi'+2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    'Hi'+2
TypeError: can only concatenate str (not "int") to str
>>> int('56')
56
>>> int(3.14)
3
>>> int('word 56')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int('word 56')
ValueError: invalid literal for int() with base 10: 'word 56'
>>> str(56)
'56'
>>> float('56')
56.0
>>> # Комментарий в одну строку
>>> ''' Несколько
        строчек
'''
' Несколько\n        строчек\n'
>>> '''Несколько
        строчек'''
'Несколько\n        строчек'
>>> """Несколько
строчек"""
'Несколько\nстрочек'
>>> '''
Это строковый литерал.
Но здесь он используется как многострочный комментарий
'''
'\nЭто строковый литерал.\nНо здесь он используется как многострочный комментарий\n'
>>> age=18
>>> name='Name'
>>> print(age)
18
>>> print(name)
Name
>>> ä=3
>>> print(ä)
3
>>> ы=2
>>> print(ы)
2
>>> a=6
>>> b=5
>>> c=a+b
>>> print(c)
11
>>> print('Сумма:',c)
Сумма: 11
>>> print('Сумма:', c)
Сумма: 11
>>> print('Сумма:',a,'+',b,'=',c)
Сумма: 6 + 5 = 11
>>> 