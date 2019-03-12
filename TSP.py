import random
import math
import numpy

class Cities:

    def __init__(self):
        self.x = int(random.randint(0, 200))
        self.y = int(random.randint(0, 200))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceTo(self, city):
        distanceX = math.fabs(self.getX() - city.getX())
        distanceY = math.fabs(self.getY() - city.getY())
        distance = math.sqrt(math.pow(distanceX, 2) + math.pow(distanceY, 2))

        return distance

    def coordinates(self):
        return self.getX() + ',' + self.getY()


class Manager:
    def __init__(self):
        self.cities = []

    def addCity(self, city):
        self.cities.append(city)

    def getCity(self, index):
        return self.cities.__getitem__(index)

    def numberOfCities(self):
        return self.cities.__len__()


class Tour:
    def __init__(self):
