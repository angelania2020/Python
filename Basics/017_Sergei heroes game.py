#Мой вариант. Не то, чтобы крутой, но условия выполняет
import random
iD=0 #global id for each object
class Person:
    id #local id declaration
    team=0 #team nubmer
    def __init__(self,t):
        global iD
        self.team=t #team selection
        self.id=iD #this objects id
        iD+=1 #id change for next object
       
       
       
class Hero(Person):
    level=1 #each hero starts with level 1
    def levelUp(self):
        self.level=self.level+1 #levelup
   
class Soldier(Person):
    def followHero(self,Hero): #soldier follows his hero
        print("Soldier #", self.id, " follows Hero #", Hero.id)
   
       
h1=Hero(1) #new heroes
h2=Hero(2)

#this was an id test
# print("Hero 1 id is:",h1.id, "and his army`s id-s")
# for a in range(len(army1)):
#     print(army1[a].id)
# print("Hero 2 id is:",h2.id, "and his army`s id-s")
# for b in range(len(army2)):
#     print(army2[b].id)
game=True
while game:
    army1=[] #and their armies
    army2=[]
    for i in range(20): #army creation
        n = random.randint(1,2)
        if n == 1:
            army1.append(Soldier(n))
        else:
            army2.append(Soldier(n))
   
    if len(army1)>len(army2):
        h1.levelUp()
        print("Hero 1 level is now ", h1.level)
        army1[random.randint(0, len(army1)-1)].followHero(h1)
    elif len(army2)>len(army1):
        h2.levelUp()
        print("Hero 2 level is now ", h2.level)
        army2[random.randint(0, len(army2)-1)].followHero(h2)
    else:
        print("The two armies are equal!")
    if int(input("To continue enter 1"))!=1:
        game=False