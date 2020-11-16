import math

pii=math.pi
print(f'Пи округлим до {pii:0.2f}')

a = 3.3568
b = 163.23
c = 24.456585
print(f'{a:10.2f}|{b:10.2f}|{c:10.2f}')
print(f'{a:<10.2f}|{b:^10.2f}|{c:>10.2f}')


a='Jüri'
b='Mari'
c='Rein'
print(f'{a.ljust(10)}|{b.center(10)}|{c.rjust(10)}')
# 10 - это параметр
a='Jüri'
b='Mari'
c='Rein'
print(f'''{a.ljust(10)}|
{b.center(10)}|
{c.rjust(10)}''')
