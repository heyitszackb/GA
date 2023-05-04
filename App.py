from initialize import initPopCoords, initFoods, initPopulation
from makeNextGen import makeNextGen
from calcPop import calcPop
from Const import POPULATION_SIZE, CROSSOVER_RATE, MUTATION_RATE
from graph import graph
from updatePopulation import updatePopulation
from spawnFood import spawnFood

from Const import WIDTH, HEIGHT, TICKS, GENERATIONS_TO_RUN
import time


import pyxel

import math

class App:
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT)
        pyxel.load("sim.pyxres")
        self.generation_num = 0
        self.generations = GENERATIONS_TO_RUN
        self.tick_num = 0
        self.width = WIDTH
        self.height = HEIGHT
        self.avg_fitnesses = []
        self.sense = []
        self.speed = []
        self.generations_arr = []
        self.population = self.run()
        self.tick_population = initPopCoords(self.population,self.width,self.height)
        self.food = initFoods(WIDTH,HEIGHT)
        pyxel.run(self.update, self.draw)

    def run(self):
        overallStart = time.perf_counter()

        population = initPopulation(POPULATION_SIZE)
        for i in range(self.generations):
            generationStart = time.perf_counter()
            population = makeNextGen(population, CROSSOVER_RATE, MUTATION_RATE)

            self.avg_fitnesses.append(calcPop(population,"fitness"))
            self.sense.append(calcPop(population,"sense"))
            self.speed.append(calcPop(population,"speed"))
            self.generations_arr.append(i)
            generationEnd = time.perf_counter()
            print("Time to run generation: " + str(i + 1) + " " + str(round(generationEnd - generationStart,2)))

        overallEnd = time.perf_counter()
        print("Total time to run: " + str(round(overallEnd - overallStart,2)))
        print("Average generation time: " + str(round((overallEnd - overallStart)/self.generations,2)))
        graph(self.generations_arr,self.avg_fitnesses, 'fitness')
        graph(self.generations_arr,self.sense, 'sense')
        graph(self.generations_arr,self.speed, 'speed')
        return population

    def update(self):
        self.tick_population,self.food = updatePopulation(self.tick_population,self.food,self.width,self.height)
        self.food = spawnFood(self.food,self.width,self.height)
        self.tick_num += 1

    def draw(self):
        pyxel.cls(0)
        for i in range(len(self.tick_population)):
            self.tick_population[i].draw()
            if self.tick_population[i].closestFood and self.tick_population[i].energy > 0:
                pyxel.line(self.tick_population[i].getCoords()[0],
                        self.tick_population[i].getCoords()[1], 
                        self.tick_population[i].closestFood.getCoords()[0],
                        self.tick_population[i].closestFood.getCoords()[1],
                        7) 
                
        for i in range(len(self.food)):
            self.food[i].draw()

        pyxel.text(5,5,"Population: " + str(len(self.tick_population)),7)
        pyxel.text(5,10,"Food: " + str(len(self.food)),7)
        pyxel.text(5,15,"Average Fitness: " + str(calcPop(self.tick_population,"fitness")),7)
        pyxel.text(5,20,"Tick Number: " + str(self.tick_num),7)