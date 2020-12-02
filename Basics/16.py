class Student:
    #атрибуты
    name='unknown'
    age=0
    #методы
    def add_Name(self,x):
        self.name=x
    def add_Age(self,x):
        self.age=x
    def display(self):
        print('Name: {} \nAge: {}'.format(self.name, self.age))
        
#объекты
newObject=Student()
newObject.add_Name(input('name'))
newObject.add_Age(input('age'))
newObject.display()





class Student2:
    #атрибуты
    name=course='unknown' #SKTVp20
    age=0
    #методы
    def __init__(self,x,y,g):
        self.name=x
        self.age=y
        self.course=g
    def display(self):
        print('Name: {} \nAge: {} \nCourse: {}'.format(self.name, self.age, self.course))

        
newObject=Student2(input('Name'),input('age'),input('course'))
newObject.display()





class Cars:
    Brand=Color='unknown'
    Year=Price=MaxSpeed=0
    def __init__(self,a,b,c,d,e):
        self.Brand=a
        self.Color=b
        self.Year=c
        self.Price=d
        self.MaxSpeed=e
    def display(self):
        print('Brand: {} \nColor: {} \nYear: {} \nPrice: {} \nMaxSpeed: {}'.format(self.Brand,self.Color,self.Year,self.Price, self.MaxSpeed))
    
newCar1=Cars(a='Opel', b='Black', c=2020, d=28000, e=200) #object
newCar2=Cars(a='BMW', b='White', c=2015, d=15000, e=150)

newCar1.display()
print()
newCar2.display()

    
