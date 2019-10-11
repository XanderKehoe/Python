class Nation:
    def __init__(self, name, continent, population, area):  # Initializer
        self.name = name
        self.continent = continent
        self.population = population
        self.area = area

    # getters
    def getName(self):
        return self.name

    def getContinent(self):
        return self.continent

    def getPopulation(self):
        return self.population

    def getArea(self):
        return self.area

    def popDensity(self):
        return self.population/self.area

    # return readable string format
    def __repr__(self):
        return '("%s", "%s", "%s", "%s")' % (self.name, self.continent, self.population, self.area)

    def __str__(self):
        return '("%s", "%s", "%s", "%s")' % (self.name, self.continent, self.population, self.area)
