from runSimulation import runSimulation
import random
from crossover import crossover
from mutate import mutate

from Const import WIDTH, HEIGHT, TICKS

def makeNextGen(population, crossover_rate, mutation_rate):
    simulatedPopulation = runSimulation(population,TICKS,WIDTH,HEIGHT)

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



# if you are dead, your genetic material has a very low chance of being passed on, but if you are
# alive, you have a very high chance of passing on your genetic material