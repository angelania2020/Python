# 2 Ангелина и Яна 03.11.20

print('Введите стороны треугольника a, b, c')
a=int(input())
b=int(input())
c=int(input())
P = a + b + c
print('Периметр треугольника:', P)

# 3 Ангелина и Яна 03.11.20

Tovar=36.75
Tovarskidka=Tovar*0.6
Tritovaraskidka=3*Tovarskidka
print('Три товара со скидкой будут стоить:', Tritovaraskidka, 'евро')

# 4 Ангелина и Яна 03.11.20

pizza=12.90
chaevije=0.1*pizza
kazdijdolzen=(pizza+chaevije)/3
print('Каждый должен заплатить:', kazdijdolzen, 'евро')

# 5 Ангелина и Яна 03.11.20

skorostrollerakmch=29.9
vremjavminutah=24
vremjavchasah=vremjavminutah/60
rasstojanije=skorostrollerakmch*vremjavchasah
print('Проехал в километрах:',rasstojanije)

# 6 Ангелина и Яна 03.11.20

a=16
b=9
c=pow(pow(a,2)+pow(b,2),0.5)
print('Гипотенуза:',round(c,2))

# 7 Ангелина и Яна 03.11.20

print('Введите время в минутах')
vremjavminutah=int(input())
chasi=vremjavminutah//60
minuti=vremjavminutah%60
vremja='{}:{}'.format(chasi,minuti)
print(vremja)


print('Введите время в минутах')
vremjavminutah=int(input())
chasi=vremjavminutah//60
minuti=vremjavminutah%60
chasi=str(chasi)
minuti=str(minuti)
print(':'.join([chasi,minuti]))

# 8 Ангелина и Яна 03.11.20

print('Введите число в десятичной системе')
a=int(input())
b=bin(a)
c=hex(a)
print('Двоичное:',b,'Шестнадцатеричное:',c)


# 9 Ангелина и Яна 03.11.20

print('Введите литры заправленного топлива')
litri=int(input())
print('Введите пройденные километры')
kilometri=int(input())
rashod1=litri/kilometri
rashod2=rashod1*100
print('Расход топлива на 100 км в среднем', round(rashod2,0), 'литров')










