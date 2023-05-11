import random

from Const import INITIAL_SENSE_UPPER_BOUND, INITIAL_SENSE_LOWER_BOUND, INITIAL_SIZE_LOWER_BOUND, INITIAL_SIZE_UPPER_BOUND, INITIAL_SPEED_LOWER_BOUND, INITIAL_SPEED_UPPER_BOUND \

def mutateSpeed(individual):
    if individual.speed == INITIAL_SIZE_LOWER_BOUND or individual.speed > INITIAL_SPEED_UPPER_BOUND:
            return individual
    else:
        num = random.randint(0,1)
        if num == 0 and individual.speed < INITIAL_SPEED_LOWER_BOUND:
            individual.setSize(individual.speed + 1)
        else:
            individual.setSize(individual.speed - 1)
    return individual


    individual.speed += random.randint(-1,1)
    return individual

def mutateSize(individual):
    if individual.getSize() == INITIAL_SENSE_LOWER_BOUND or individual.getSize() > INITIAL_SIZE_UPPER_BOUND:
            return individual
    else:
        num = random.randint(0,1)
        if num == 0 and individual.size < INITIAL_SENSE_LOWER_BOUND:
            individual.setSize(individual.getSize() + 1)
        else:
            individual.setSize(individual.getSize() - 1)
    return individual

def mutateSense(individual):
    if individual.sense == INITIAL_SENSE_LOWER_BOUND or individual.sense > INITIAL_SENSE_UPPER_BOUND:
            return individual
    else:
        num = random.randint(0,1)
        if num == 0 and individual.sense < INITIAL_SENSE_UPPER_BOUND:
            individual.sense(individual.sense + 1)
        else:
            individual.sense(individual.sense - 1)
    return individual


def mutateScales(individual):
    individual.scale = [round(random.uniform(-1,1),2), round(random.uniform(-1,1),2)]
    return individual

def mutate(individual, mutation_rate):
    random_mutation_num = random.random()
    if random_mutation_num < mutation_rate:
        # random_func = random.choice([mutateSpeed,mutateSize,mutateScales])
        # random_func(individual)
        individual = mutateScales(individual)
        individual = mutateSize(individual)
        individual = mutateSpeed(individual)
    return individual