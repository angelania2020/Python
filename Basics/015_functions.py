def bigger(a,b):
    if a>b:
        print(a)
    else:
        print(b)
        
bigger(5,6)

#2
def person(name,age):
    print(name,'is',age,'years old')
    
person(age=23, name='John')
person(age=input('age'), name=input('Name'))

#3
def space(planet_name, center='Star'):
    print(planet_name, 'is orbiting a', center)
    
space('Mars')
space('Mars', 'Black Hole')

#4
def unknown(*args):
    for argument in args:
        print(argument)

unknown('hello','world')
unknown(1,2,3,4,5)
unknown()

#return
def bigger(a,b):
    if a>b:
        return a
    return b

num=bigger(23,42)
print(num)

#local, global
age=44 #global

def info():
    print(age)
    

def local_info():
    age=22
    print(age)
    
info()
local_info()


#global
age=13 #глобальная переменная
def get_older():#изменяет глоб.пер.
    global age
    age += 1
    
print(age) #напечатает 13
get_older() #увеличиваем age на 1
print(age) #напечатает 14


# факториал числа
def fact(num):
    if num == 0: #сравнение
        return 1
    else:
        return num*fact(num -1)
print(fact(5))



def rectangle_area_finder(a,b):
    
    '''

    Parameters
    ----------
    a : rectangle first side.
    b : rectangle second side.

    Returns rectangle area
    -------

    '''
    return a*b

print('a * b = ', rectangle_area_finder(15,3))

rectangle_area_finder(15,3)




def my_contacts(name,age,city,sex):
    print(name)
    print(age)
    print(city)
    print(sex)
    
    

my_contacts('Angelina', 27,'Sillamäe', 'F')
print()
my_contacts('Denis', 10, 'Sillamäe', 'M')




def triangle_area(base, height):
#Определение площали треугольника
    area=(base*height)/2
    print('Triangle area is:', area)

triangle_area(base=float(input('Base')),height=float(input('Height')))
