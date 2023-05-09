import time
from graph import graph
from Const import POPULATION_SIZE, CROSSOVER_RATE, MUTATION_RATE, WIDTH, HEIGHT, GENERATIONS_TO_RUN
from initialize import initFoods, initPopulation, initPopCoords
from makeNextGen import makeNextGen
from calcPop import calcPop
from sortPop import sortPop


class MainRunner:
    def __init__(self, generations_to_return):
        self.generations_to_return = generations_to_return
        self.generations = GENERATIONS_TO_RUN
        self.width = WIDTH
        self.height = HEIGHT
        self.avg_fitnesses = []
        self.sense = []
        self.speed = []
        self.generations_arr = []
        self.generation_data = []
        self.population = self.run()

    def run(self):
        overallStart = time.perf_counter()

        population = initPopulation(POPULATION_SIZE)
        for i in range(self.generations):
            generationStart = time.perf_counter()
            population = makeNextGen(population, CROSSOVER_RATE, MUTATION_RATE)

            if i in self.generations_to_return:
                self.generation_data.append([i,population])
                self.generations_to_return.remove(i)

            generationEnd = time.perf_counter()
            print("Time to run generation: " + str(i + 1) + " " + str(round(generationEnd - generationStart,2)))
    
    def getGenerationData(self):
        return self.generation_data




        #     self.avg_fitnesses.append(calcPop(population,"fitness"))
        #     self.sense.append(calcPop(population,"sense"))
        #     self.speed.append(calcPop(population,"speed"))
        #     self.generations_arr.append(i)

        # overallEnd = time.perf_counter()
        # print("Total time to run: " + str(round(overallEnd - overallStart,2)))
        # print("Average generation time: " + str(round((overallEnd - overallStart)/self.generations,2)))
        # graph(self.generations_arr,self.avg_fitnesses, 'fitness')
        # graph(self.generations_arr,self.sense, 'sense')
        # graph(self.generations_arr,self.speed, 'speed')
        return population