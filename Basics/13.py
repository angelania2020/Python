#1
a=input('Please insert elements of the list using spacebar: ').split()
for i in range(0,len(a),2):
    print(a[i])

#2
a=input('Please insert elements of the list using spacebar: ').split()
print('Even elements of the list: ')
for i in range(0,len(a)):
    if int(a[i])%2==0:
        print(a[i], end=' ')

s=input('Please insert elements of the list using spacebar: ')
a=[int(s) for s in s.split()]
for i in a:
    if int(i)%2==0:
        print(i,end=' ')
        
#3 Boljshe predidushego
a=[int(i) for i in input('Please insert elements of the list using spacebar: ').split()]
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        print(a[i])
        
#4 Sosedi odnogo znaka
a=[int(i) for i in input('Please insert elements of the list using spacebar: ').split()]
for i in range(1,len(a)):
    if a[i]>0 and a[i-1]>0:
        print(a[i-1],a[i])
    elif a[i]<0 and a[i-1]<0:
        print(a[i-1],a[i])
        break
    
a=[int(i) for i in input().split()]
for i in range(1,len(a)):
    if a[i-1]*a[i]>0:
        print(a[i-a],a[i])
        break

#5
a=[int(i) for i in input('Please insert elements of the list using spacebar: ').split()]
counter=0
for i in range(1,len(a)):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        counter+=1
print(counter)

a=[int(i) for i in input('Please insert elements of the list using spacebar: ').split()]
counter=0
for i in range(1,len(a)-1):
    if a[i-1]<a[i]>a[i+1]:
        counter+=1
print(counter)

#6
a=[int(i) for i in input('Please insert elements of the list using spacebar: ').split()]
maxindex=a.index(max(a))
maximum=max(a)
print('Maximum element in the list is: {}.'.format(maximum),'Its index is: {}.'.format(maxindex))

a=[int(i) for i in input('Please insert elements of the list using spacebar: ').split()]
for i in range(len(a)):
    if a[i]==max(a):
        print('max(a)',max(a),'[i],',i)

#7!!!moja poka ne rabotajet
a=[int(i) for i in input('Please insert the heights (less than 200 cm) of children: ').split()]
X=int(input('Enter Peter\'s height in cm (less than 200 cm): '))
a.sort(reverse=True)
a.append(X)
a.sort(reverse=True)
print(a)
peter=a.index(X)
print(peter)

a=[int(i) for i in input('Please enter the heights (less than 200 cm) of children in descending order: ').split()]
X=int(input('Enter Peter\'s height in cm (less than 200 cm): '))
pos=0
while pos<len(a) and a[pos]>=X:
    pos+=1
print(pos+1)

#8
a=[int(i) for i in input('Enter elements: ').split()]
num_distinct=1
for i in range(0,len(a)-1):
    if a[i]!=a[i+1]:
        num_distinct+=1
print(num_distinct)