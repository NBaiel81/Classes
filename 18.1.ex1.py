class Planet:
    def __init__(self, name,size,color):
        self.name=name
        self.size=size
        self.color=color
        self.humanity=True
        self.oxygen=True
        self.water=False
        self.temp=0
        self.burger=False
    def set_humanity(self):
        if self.humanity:
            self.humanity=False
            self.oxygen=False
        else:
            self.humanity=True
            self.oxygen=True
    def set_water(self):
        if self.size=="middle" or self.size=='great':
            self.water=True
        else:
            self.water=False
        if self.water:
            self.burger=True
        else:
            self.burger=False



planet=Planet('Maxim','middle','tiffany')
print(planet.name,planet.color,planet.humanity,planet.water,planet.burger)
planet.set_humanity()
planet.set_water()
print(planet.name,planet.color,planet.humanity,planet.water,planet.burger)
planet.set_humanity()
planet.set_water()
print(planet.name,planet.color,planet.humanity,planet.water,planet.burger)
planet.set_humanity()
planet.set_water()
print(planet.name,planet.color,planet.humanity,planet.water,planet.burger)
planet.set_water()

