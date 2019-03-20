import random
import numpy as np
import panda as pd 
import math

class City:
    def __init__(self):
        self.x = x
        self.y = y

    def distance(self, city):
        disX = pow(math.fabs(self.x - city.x), 2)
        disY = pow(math.fabs(self.y - city.y), 2)
        return math.sqrt(disX + disY)


class Fitness:
    def __init__(self):
        self.road = road
        self.distance = 0
        self.fitness = 0

    def road_distance(self):
        if self.fitness == 0:
            path = 0

            for i in range(0, len(self.road)):
                fromCity = self.road[i]
                toCity = None
                if i + 1 < len(self.road):
                    toCity = self.road[i + 1]
                else:
                    toCity = self.road[0]

                path += fromCity.distance(toCity)
            self.distance = path
        return self.distance

    def road_fitness(self):
        if self.fitness == 0:
            self.fitness = 1/float(self.road_distance())
        return self.fitness


def createRoad(cityList):
    road = random.sample(cityList, len(cityList))
    return road

def population(pSize, cityList):
    population = []

    for i in range(pSize):
        population.append(createRoad(cityList))
    return population

def fitnessEvaluation(population):
    fitResults = []
    for i in range(len(population)):
        fitResults[i] = Fitness(population[i].road_fitness())

    return sorted(fitResults, reverse= True)

def selection(popRank, bestSize):
    selResults = []
    df = pd.DataFrame(np.array(popRank), columns=["Index", "Fitness"])
    df["cum_sum"] = df.Fitness.cumsum()
    df["cum_perc"] = 100* df.cum_sum/df.Fitness.sum()

    for i in range(bestSize):
        selResults.append(popRank[i][0])
    for i in range(len(popRank) - bestSize):
        pick = 100*random.random()
        for i in range(len(popRank)):
            if pick <= df.iat[i,3]:
                selResults.append(popRank[i][0])
                break
    return selResults

def breed(adult1, adult2):
    child = []
    childA1 = []
    childA2 = []

    geneA = int(random.random() * len(adult1))
    geneB = int(random.random() * len(adult2))


    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childA1.append(adult1[i])

    childA2 = [item for item in adult2 if item not in childA1]

    child = childA1 + childA2

    return child

def breedPopulation(mating, bestSize):
        children = []
        length = len(mating) - bestSize
        pool = random.sample(mating, len(mating))

        for i in range(bestSize):
            children.append(mating[i])

        for i in range(length):
            child = breed(pool[i], pool[len(mating) - i - 1])
            children.append(child)
        return children

def mutation(indiv, mutRate):
    for swapped in range(len(indiv)):
        if random.random() < mutRate:
            swapWith = int(random.random() * len(indiv))

            city1 = indiv[swapped]
            city2 = indiv[swapWith]

            indiv[swapped] = city2
            indiv[swapWith] = city1

    return indiv

def mutatePopulation(pop, mutRate):
    mutatedPop = []
    for ind in range(len(pop)):
        mutatedInd = mutation(pop[ind], mutRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

def nextGeneration(curGen, bestSize, mutRate):
    popRank = fitnessEvaluation(curGen)
    selResults = selection(popRank, bestSize)
    pool = mating(curGen, selResults)
    children = breedPopulation(pool, bestSize)
    nextGen  = mutatePopulation(children, mutRate)
    return nextGen

def geneticAlgo(pop, popSize, bestSize, mutRate, generations):
    pop = population(popSize, pop)
    print("Initial distance: " + str(1/fitnessEvaluation(pop)[0][1]))

    for i in range(generations):
        pop = nextGeneration(pop, bestSize, mutRate)

    print("Final Distance: " + str(1/fitnessEvaluation(pop)[0][1]))
    bestRoadIndex = fitnessEvaluation(pop)[0][0]
    bestRoad = pop[bestRoadIndex]

    return bestRoad



city = []
for i in range(100):
    city.append(City(x = int(random.random() * 200), y = int(random.random() * 200)))
geneticAlgo(pop=city, popSize=100, mutRate= 0.02, bestSize=20, generations=500)
