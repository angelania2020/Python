# f(x)=x*2
def f(x):
    return x*2
f(2)
result=f(2)
print(result)

def f(x):
    return x+1
z=f(4)
if z==5:
    print('z is 5')
else:
    print('z is not 5')
    
def f():
    return 1+1
result=f()
print(result)

def f(x,y,z):
    return x+y+z
result=f(1,2,3)
print(result)

def f():
    z=1+1
result=f()
print(result)

len('Monty')

len('Python')

str(100)

int('1')

float(100)

int('110')

int(20.54)

float('16.4')

float(99)

int('Prince')

age=input('Insert your age: ')
int_age=int(age)
if int_age<21:
    print('Great job!')
else:
    print('You\'re so old!')
    
def even_odd(x):
    if x%2==0:
        print('even')
    else:
        print('odd')
even_odd(2)
even_odd(3)


def even_odd():
    n=input('Please insert a number: ')
    n=int(n)
    if n%2==0:
        print('n is even.')
    else:
        print('n is odd')
even_odd()
even_odd()
even_odd()

# Optional parameters
def f(x=2):
    return x**x
print(f())
print(f(4))

def add_it(x,y=10):
    return x+y
result=add_it(2)
print(result)

# Global variables
x=1
y=2
z=3
def f():
    print(x)
    print(y)
    print(z)
f()

# Local variables
# Erase all previous variables first
# Result: NameError: name 'x' is not defined
def f():
    x=1
    y=2
    z=3
print(x)
print(y)
print(z)

def f():
    x=1
    y=2
    z=3
    print(x)
    print(y)
    print(z)
f()

# NameError: name 'x' is not defined
if x>100:
    print('x is greater than 100')


x=100
def f():
    x=5
    x+=1
    print(x)
f() #6

# Changing global variable inside a function
x=100
def f():
    global x
    x+=1
    print(x)
f() #101

a=input('Please enter a number: ')
b=input('Please enter one more number: ')
a=int(a)
b=int(b)
print(a/b) #10/0 ZeroDivisionError: division by zero


a=input('Please enter a number: ')
b=input('Please enter one more number: ')
a=int(a)
b=int(b)
try:
    print(a/b) #'seven'|'one' ValueError: invalid literal for int() with base 10: 'seven'
except ZeroDivisionError:
    print('b cannot be a zero.')
 
try:
    a=input('Please enter a number: ')
    b=input('Please enter one more number: ')
    a=int(a)
    b=int(b)
    print(a/b)
except(ZeroDivisionError,ValueError):
    print('Input error.')

#Result: NameError: name 'c' is not defined.
#Do not use variables (defined in try) in except
try:
    10/0
    c='I am always undefined.'
except ZeroDivisionError:
    print(c)
    
def add(x,y):
    '''
    Outputs x+y.
    :parameter x: integer.
    :parameter y: integer.
    :return: sum of integers x and y.
    '''
    return x+y
add(5,8)

#Bad
x=100
print(x)

#Good
print(100)

#1
def squared():
    x=int(input('Enter a number: '))
    return x**2
print(squared())

def squared(x):
    return x ** 2
print(squared(7))

#2
def string(x):
    print(x)
string('Hello')

def print_string(string):
    print(string)
print_string("Проверка: 1, 2, 3.")

#3
def f(x,y,z,a=5,b=7):
    try:
        return (x-b)*(y-a)/z
    except ZeroDivisionError:
        print('z cannot be a zero')
print(f(3,0,1))
print(f(3,0,1,7,5))
print(f(4,3,0))

def add_mult(a,b,c,x=100,z=1000):
    return a + b + c * x * z
result = add_mult(10, 15, 25)
print(result)

#4

