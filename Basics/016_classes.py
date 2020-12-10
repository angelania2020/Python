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


class Cat:
    Name='unknown'
    Color='unknown'
    Breed='unknown'
    Weight=0
    def __init__(self,a,b,c,d):
        self.Name=a
        self.Color=b
        self.Breed=c
        self.Weight=d
    def meow(self):
        print('Meow!')
    def display(self):
        print('Name: {} \nColor: {} \nBreed: {} \nWeight: {}'.format(self.Name,self.Color,self.Breed,self.Weight))

    
    
newCat1=Cat(a='Rizhik', b='Red', c='Persian', d=4)
newCat2=Cat(a='Sonja', b='Grey', c='Scottish Fold', d=3.5)

newCat1.display()
print()
newCat1.meow()
print()
print()
newCat2.display()
print()
newCat2.meow()



class Monster:
    name='unknown'
    health=0
    def __init__(self,a,b):
        self.name=a
        self.health=b
    def decrease_health(self,amount):
        self.health-=amount
        print(self.health)
        if self.health<0:
            print('Monster is dead.')
            
newMonster1=Monster('Zubastik', 100)
newMonster1.decrease_health(90)
newMonster1.decrease_health(11)
    


class Animals:
    def __init__(self,w,s,c,f):
        self.weight=w
        self.size=s
        self.color=c
        self.feeds=f
        
class Birds(Animals):
    def get_bird(self,wings,feathers):
        self.wings=wings
        self.feathers=feathers
    def show_bird(self):
        print(self.wings,self.feathers,self.size)
    
class Fish(Animals):
    def get_fish(self,fins,scales):
        self.fins=fins
        self.scales=scales
    def show_fish(self):
        print(self.fins,self.scales,self.color)
        
Penguin=Birds('10 kg','королевский','белый', 'рыба')
Penguin.get_bird('несгибающиеся','как чешуя')
Penguin.show_bird()

Lastochka=Birds('18 g','маленький','черный', 'насекомые')
Lastochka.get_bird('острые','обычные')
Lastochka.show_bird()

Akula=Fish('600 Kg','огромный','серый', 'другая рыба')
Akula.get_fish('огромные','плакоидная')
Akula.show_fish()

Ugor=Fish('3 kg','средний','серый', 'мальки рыб')
Ugor.get_fish('длинные','мелкая')
Ugor.show_fish()
