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


