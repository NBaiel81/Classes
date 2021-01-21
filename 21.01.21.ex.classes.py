class Beaver:
    finished_bridges = 0
    def __init__(self, name, age, weight, power):
        self.name = name
        self.age = age
        self.weight = weight
        self.power = power
        if self.age>=11:
            self.power-=5

    def __str__(self):
        return "{} {}".format(self.name, self.age)

class Bridge:

    def __init__(self, legth, weight):
        self.length = legth
        self.weight = weight
        self.material = 'tree'

    def building(self, team:list):
        group_power=0
        for beaver in team:
            group_power+=(beaver.weight+beaver.power)
        print("power of beavers:",group_power,"needed power to create bridge:",bridge.weight+bridge.length)
        if group_power> self.weight + self.length:
            print("Мост успешно создан")
            Beaver.finished_bridges+=1
        else:
            print("Команда слишком слабая")



beaver1 = Beaver(name='Bobrik', age=5, weight=9, power=10)
beaver2 = Beaver(name='Musya', age=7, weight=20, power=15)
beaver3 = Beaver(name='Aktan', age=8, weight=23, power=18)
beaver4 = Beaver(name='Maksim', age=12, weight=43, power=20)
beaver5 = Beaver(name='Trump', age=9, weight=23, power=20)
bridge = Bridge(legth=10, weight=100)
beaver_team=[beaver1, beaver2, beaver3, beaver4, beaver5]
bridge.building(beaver_team)


print(beaver1)
print(bridge.building)