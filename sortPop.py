def sortPop(population):
    """Sorts the population by fitness"""
    population.sort(key=lambda x: x.getFitness(), reverse=True)
    for i in range(len(population)):
        population[i].is_best_individual = False
    population[0].is_best_individual = True
    return population