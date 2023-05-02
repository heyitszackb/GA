from initialize import initPopCoords, initFoods, initPopulation
from makeNextGen import makeNextGen
from calcPop import calcPop
from Const import POPULATION_SIZE, CROSSOVER_RATE, MUTATION_RATE
from graph import graph
from updatePopulation import updatePopulation
from spawnFood import spawnFood

from Const import WIDTH, HEIGHT, TICKS, GENERATIONS_TO_RUN


import pyxel

import math

class App:
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT)
        self.generation_num = 0
        self.generations = GENERATIONS_TO_RUN
        self.tick_num = 0
        self.width = WIDTH
        self.height = HEIGHT
        self.avg_fitnesses = []
        self.sense = []
        self.generations_arr = []
        self.population = self.run()
        self.tick_population = initPopCoords(self.population,self.width,self.height)
        self.food = initFoods(WIDTH,HEIGHT)
        pyxel.run(self.update, self.draw)

    def run(self):
        population = initPopulation(POPULATION_SIZE)
        for i in range(self.generations):
            print("Generation: " + str(i + 1))
            population = makeNextGen(population, CROSSOVER_RATE, MUTATION_RATE)

            self.avg_fitnesses.append(calcPop(population,"fitness"))
            self.sense.append(calcPop(population,"sense"))
            self.generations_arr.append(i)
        # graph(self.generations_arr,self.avg_fitnesses)
        graph(self.generations_arr,self.sense)
        return population

    def update(self):
        self.tick_population,self.food = updatePopulation(self.tick_population,self.food,self.width,self.height)
        self.food = spawnFood(self.food,self.width,self.height)
        self.tick_num += 1

    def draw(self):
        pyxel.cls(0)
        for i in range(len(self.tick_population)):
            x,y = self.tick_population[i].getCoords()
            pyxel.circ(x,y,self.tick_population[i].getSize(),7)
            if self.tick_population[i].closestFood:
                pyxel.line(self.tick_population[i].getCoords()[0],
                        self.tick_population[i].getCoords()[1], 
                        self.tick_population[i].closestFood.getCoords()[0],
                        self.tick_population[i].closestFood.getCoords()[1],
                        7) 
            # pyxel.circb(self.tick_population[i].getCoords()[0],
            #             self.tick_population[i].getCoords()[1],
            #             self.tick_population[i].sense, 4)
                
        for i in range(len(self.food)):
            x,y = self.food[i].getCoords()
            pyxel.circ(x,y,self.food[i].size,8)

        pyxel.text(5,5,"Population: " + str(len(self.tick_population)),7)
        pyxel.text(5,10,"Food: " + str(len(self.food)),7)
        pyxel.text(5,15,"Average Fitness: " + str(calcPop(self.tick_population,"fitness")),7)
        pyxel.text(5,20,"Tick Number: " + str(self.tick_num),7)