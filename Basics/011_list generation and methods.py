a=[0 for i in range(5)]
print(a)

n=5
b=[i**2 for i in range(n)]
print(b)

from random import randrange
n=10
c=[randrange(1,10) for i in range(n)]
print(c)

from random import randrange
n=int(input('Please insert number of elements that will be in the list: '))
c=[randrange(1,10) for i in range(n)]
print(c)

a=[1,2,3]
b=[4,5]
c=a+b
d=b*3
print(c,d)

s='ab12c59p77dq'
digits=[int(i) for i in s if '0'<=i<='9']
digits.sort()
print(digits)
digits.sort(reverse=True)
print(digits)


#split; we will get strings
print('Please insert elements of the list using spacebar:')
s=input()
a=s.split()
print(a)

#split: we will get numbers
a=input('Please insert elements of the list using spacebar: ').split()
for i in range(len(a)):
    a[i]=int(a[i])
print(a)

#Via generator, v skobkah ukazivaem po kakomu razdelitjelu mi razdeljajem !!!
a=[int(s) for s in input('Please insert elements of the list using spacebar: ').split()]
print(a)

#join
a=['red', 'green', 'blue']
print(''.join(a))

a=['red', 'green', 'blue']
print(', '.join(a))

b=[1,2,5]
print(''.join([str(i) for i in b])) #Делаем из чисел строку


#Srez
numbers=[23,63,72,10,24,98]
print(numbers[1:4]) #63, 72, 10
print(numbers[1:]) #63, 72, 10, 24, 98
print(numbers[:4]) #23, 63, 72, 10
print(numbers[:]) #23, 63, 72, 10, 24, 98
print(numbers)

numbers=[23,63,72,10,24,98]
numbers.extend([0,100])
numbers.insert(6, 25) #на 6ую позицию вставит 25
print(numbers)

#Hotim poluchitj chjotnije chisla
print('Please insert elements of the list using spacebar: ')
a=input().split()
print(a)
print('Even numbers from the list:')
for i in range(0,len(a)): #ot index 0
    if int(a[i])%2==0:
        print(a[i], end=' ')
        
print('Please insert elements of the list using spacebar: ')
a=input().split()
print('Even numbers from the list:')
for i in range(0,len(a)): #ot index 0
    if int(a[i])%2==0:
        print(a[i]) #v stolbik
        
#Vidjorgivajem chjotnije i nechjotbije indexi.
print('Please insert elements of the list using spacebar: ')
a=input().split()
print('Even indexes contain:')
for i in range(0,len(a),2): 
        print(a[i])
        
print('Please insert elements of the list using spacebar: ')
a=input().split()
print('Odd indexes contain:')
for i in range(1,len(a),2): 
        print(a[i])
#Out:
#1
#3


print('Please insert elements of the list using spacebar: ')
s=input()
a=[int(s) for s in s.split()]
print('Odd indexes contain:')
print(a[1::2])


print('Please insert elements of the list using spacebar: ')
s=input().split()
print('Odd indexes contain:')
print(s[1::2]) #['1', '3'] list with strings