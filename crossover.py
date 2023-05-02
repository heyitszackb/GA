import random
from Creature import Creature

def crossover(parent1,parent2, crossover_rate):
    random_crossover_num = random.random()
    if random_crossover_num < crossover_rate:
        newScale = [parent1.scale[0] + parent2.scale[0]//2 , parent1.scale[1] + parent2.scale[1]//2]
        
        newIndividual = Creature((parent1.getSize() + parent2.getSize())//2,
                                 (parent1.speed + parent2.speed)//2,
                                 newScale,
                                 (parent1.sense + parent2.sense)//2)
    else:
        newIndividual = parent1
    return newIndividual