class Person:
    def __init__(self,name,race):
        self.name=name
        self.race=race
        if race=="fairy":
            self.health=10
            self.mana=2000
        elif race=="fairy":
            self.health=200
            self.mana=100
        else:
            self.health=150
            self.mana=150
        self.power=0
        self.armor=0
        self.damage=0
        self.level=0
        self.exp=0
        self.range=1
        self.position=0
        print('Character successfully created!')

    def descripyion(self):
        print(f"Имя: {self.name}, Мана: {self.mana}, Здоровье: {self.health},Доспехи: {self.armor},Раса: {self.race}, Сила: {self.power}, Урон: {self.damage}, Уровень: {self.level}")

    def level_up(self,exp):
        self.exp+=exp
        if self.exp==100:
            self.level+=1
            choose=input('Choose characteristic:')
            if choose=="power":
                self.power+=1
            elif choose=='damage':
                self.damage+=1
            elif choose=='armor':
                self.armor+=1
            else:
                self.power += 0.3

    def wear(self,cloth):
        if cloth=='pentaarmor':
            self.armor+=20
        elif cloth=="legendary dress":
            self.armor+=100
            self.health+=50
        elif cloth=='witch jacket':
            self.mana+=120
    def set_weapon(self,weapon):
        if weapon=='sword':
            self.power+=1
            self.range=2
        elif weapon=='axe':
            self.power+=1
            self.damage+=2
            self.range=2
        elif weapon=="bow":
            self.power+=1
            self.damage+=1
            self.mana+=1
            self.range=200

    def move(self):
        self.position+=1

    def attack(self,object):
        if (self.position - object.position) <=self.range:
            object.health -= self.damage
            print("monster's health after the attack", object.health)

class Monster:
    def __init__(self,position):
        self.position=position
        self.health=20

monster=Monster(2)

warrior1=Person('Tiffany','goblin')
warrior1.level_up(100)
warrior1.set_weapon("bow")
warrior1.wear('witch jacket')
warrior2=Person('Bloom','fairy')

warrior1.attack(monster)
warrior1.attack(monster)

print(monster.health,monster.position)
# warrior1.descripyion()
# warrior2.descripyion()