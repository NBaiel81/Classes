class Rocket():
    def __init__(self,name,model,year,fuel_capacity,length,weight,food_capacity,people_capacity=None):
        self.name=name
        self.model=model
        self.year=year
        self.fuel_capacity=fuel_capacity
        self.length=length
        self.weight=weight
        self.people_capacity=people_capacity
        self.force=0
        self.distance=0
        if self.people_capacity!=None:
            self.food_capacity = food_capacity

    def __str__(self):
        return f"name:{self.name}, model:{self.model}, year:{self.year}, fuel_capacity:{self.fuel_capacity}, length:{self.weight}, food_capacity:{self.food_capacity}, people:{self.people_capacity}"
    def fly(self):
        self.force = (self.weight + self.length)
        self.distance = 0
        if self.force >= self.fuel_capacity:
            self.distance = self.fuel_capacity - self.force
            return self.distance
        else:
            return 0


class Type(Rocket):
    def __init__(self,name,model,year,fuel_capacity,length,weight,food_capacity,rock_type,people_capacity=None):
        super().__init__(name, model, year, fuel_capacity, length, weight, food_capacity, people_capacity)
        self.rock_type=rock_type
        if self.rock_type=="lightbattleship":
            self.speed=100
        elif self.rock_type=="hugebattleship":
            self.speed=50
        elif self.rock_type=='civilianship':
            self.speed=25

class Time:

    def __init__(self,fly,type):
        self.distance = fly
        self.speed = type.speed
        self.time = self.distance / self.speed
        print(f"distance:{self.distance},speed:{self.speed}")
        print(f"time:{self.time}")




rocket1=Rocket("Space","X","2020",100,10,300,20,2)
rocket2=Type(name='FaLCON 21',model='X',year=2021,fuel_capacity=20,
                   length=200,weight=100,food_capacity=11,rock_type='civilianship')

time=Time(rocket2.fly(),rocket2)






