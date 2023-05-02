def calcPop(population,gene):
    total_fitness = 0
    for individual in population:
        if gene == "fitness":
            total_fitness += individual.getFitness()
        elif gene == "speed":
            total_fitness += individual.speed
        elif gene == "size":
            total_fitness += individual.getSize()
        elif gene == "sense":
            total_fitness += individual.sense
    return total_fitness / len(population)