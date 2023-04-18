import pyxel
import random
import matplotlib.pyplot as plt


POPULATION_SIZE = 2000
MUTATION_RATE = 0.001
CROSSOVER_RATE = 0.7
GENERATIONS = 500

# [0,1,2,3,4]

class Creature:
    def __init__(self, size):
        self.size = size
    
    def getFitness(self):
        return self.size

    def setSize(self,newSize):
        self.size = newSize
    
    def getSize(self):
        return self.size


def initPopulation(population_size):
    population = []
    for _ in range(population_size):
        population.append(Creature(random.randint(1,21)))
    return population

# def fitness(individual):
#     return individual[0]
# for i in range(1,21):
#     print(random.randint(1,3))

def calcPopFit(population):
    total_fitness = 0
    for individual in population:
        total_fitness += individual.getFitness()
    return total_fitness / len(population)


def runSimulation(population):
    return population

def makeNextGen(population, crossover_rate, mutation_rate):
    # run a simulation on the population for one generation
    # //
    simulatedPopulation = runSimulation(population)
    # calculate the fitness for each individual after the generation runs

    # create the new generation from the most fit individuals
    population_size = len(simulatedPopulation)
    new_gen = []
    for i in range(population_size):
        selected_parents = []
        for i in range(2):
            index1 = 0
            index2 = 0
            while index1 == index2:
                index1 = random.randint(0,population_size-1)
                index2 = random.randint(0,population_size-1)
            parent1 = population[index1]
            parent2 = population[index2]
            if parent1.getFitness() > parent2.getFitness():
                selected_parents.append(parent1)
            else:
                selected_parents.append(parent2)
        child = crossover(selected_parents[0], selected_parents[1], crossover_rate) 
        new_gen.append(mutate(child, mutation_rate))

    return new_gen


def crossover(parent1,parent2, crossover_rate):
    random_crossover_num = random.random()
    if random_crossover_num < crossover_rate:
        newIndividual = Creature((parent1.getSize() + parent2.getSize())//2)
    else:
        newIndividual = parent1
    return newIndividual



def mutate(individual, mutation_rate):
    random_mutation_num = random.random()
    if random_mutation_num < mutation_rate:
        if individual.getSize() == 1 and individual.getSize() > 21:
            return individual
        else:
            num = random.randint(0,1)
            if num == 0 and individual.size < 21:
                individual.setSize(individual.getSize() + 1)
            else:
                individual.setSize(individual.getSize() - 1)
    return individual



def run():
    x = []
    y = []
    population = initPopulation(POPULATION_SIZE)
    for i in range(GENERATIONS):
        population = makeNextGen(population, CROSSOVER_RATE, MUTATION_RATE)
        x.append(i)
        gen_fitness = calcPopFit(population)
        y.append(gen_fitness)
    return x,y

def graph(x, y):
    plt.scatter(x,y)
    plt.xlabel('Generation Number')
    plt.ylabel('Fitness')
    plt.title('Fitness as a function of generation number')
    plt.show()

# generation_nums, generation_fitness = run()
# graph(generation_nums,generation_fitness)


# G R A P H I N G

import pyxel

import math

class App:
    def __init__(self):
        # pyxel.init(int((math.sqrt(POPULATION_SIZE))*20), int((math.sqrt(POPULATION_SIZE))*20))
        pyxel.init(416,544)
        self.population = initPopulation(POPULATION_SIZE)
        self.generation_num = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.population = makeNextGen(self.population, CROSSOVER_RATE, MUTATION_RATE)
        self.generation_num += 1

    def draw(self):
        pyxel.cls(0)
        for i in range(len(self.population)):
            # for every circle in the population, draw it on the screen in a 10x10 grid with no space between them
                    # calculate x and y coordinates for the circle based on its position in the grid
            x = (i % int(math.sqrt(POPULATION_SIZE))) * 20
            y = (i // int(math.sqrt(POPULATION_SIZE))) * 20
            
            # draw the circle using the Pyxel library
            pyxel.circ(x + 10, y + 10, self.population[i].getSize()/2, 7)

App()