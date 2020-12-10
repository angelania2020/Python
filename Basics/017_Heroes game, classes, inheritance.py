from random import randint
            
class Person:
    number=1
    def __init__(self,team):
        self.id=Person.number
        self.team=team
        Person.number+=1
     
class Hero(Person):
    level=0
    def increase_level(self,amount):
        self.level+=amount
    def show_Hero(self):
        print('Hero id: {}.'.format(self.id), 'Team: {}.'.format(self.team), 'Level: {}.'.format(self.level))
    
class Soldier(Person):
    def follow_hero(self):
        print('Я иду за героем номер: {}!'.format(self.team))
    def show_Soldier(self):
        print('Soldier id: {}.'.format(self.id), 'Team: {}.'.format(self.team))
        
Hero1=Hero(1)
Hero2=Hero(2)

Army1=[]
Army2=[]

for i in range(20):
 n = randint(1, 2)
 if n == 1:
     Army1.append(Soldier(n))
 else:
     Army2.append(Soldier(n))
     
a1=len(Army1)
a2=len(Army2)
print('В первой армии:', a1, 'солдат.')
print('Во второй армии:', a2, 'солдат.')
print()
if a1>a2:
    Hero1.increase_level(1)
elif a2>a1:
    Hero2.increase_level(1)
else:
    pass
    
Hero1.show_Hero()
Hero2.show_Hero()
print()
Army1[0].show_Soldier()
Army1[0].follow_hero()
print()
print('Soldier id: {}.'.format(Army1[0].id), 'Hero id: {}.'.format(Hero1.id))