from initialize import initPopCoords, initFoods, initPopulation
from makeNextGen import makeNextGen
from calcPop import calcPop
from Const import POPULATION_SIZE, CROSSOVER_RATE, MUTATION_RATE
from graph import graph
from updatePopulation import updatePopulation
from spawnFood import spawnFood
from sortPop import sortPop

from Const import WIDTH, HEIGHT, TICKS, GENERATIONS_TO_RUN
import time


import pyxel

import math

class App:
    def __init__(self, population, generation_num):
        self.population = initPopCoords(population, WIDTH, HEIGHT)
        self.generation_num = generation_num
        self.tick_num = 0
        self.food = initFoods(WIDTH,HEIGHT)
        self.width = WIDTH
        self.height = HEIGHT
        pyxel.init(WIDTH,HEIGHT)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.population,self.food = updatePopulation(self.population,self.food,self.width,self.height)
        self.food = spawnFood(self.food,self.width,self.height)
        self.population = sortPop(self.population)
        self.tick_num += 1
        # if self.tick_num == TICKS:
        #     pyxel.stop()

    def draw(self):
        pyxel.cls(0)
        thirdOfColors = int(len(self.population)/3)
        for i in range(len(self.population)):
            if i <= thirdOfColors: self.population[i].color = 1
            elif i <= thirdOfColors*2: self.population[i].color = 5
            else: self.population[i].color = 6
            self.population[i].draw()
            
            if self.population[i].closestFood and self.population[i].energy > 0:
                pyxel.line(self.population[i].getCoords()[0],
                        self.population[i].getCoords()[1], 
                        self.population[i].closestFood.getCoords()[0],
                        self.population[i].closestFood.getCoords()[1],
                        self.population[i].color) 
                
        for i in range(len(self.food)):
            self.food[i].draw()

        pyxel.text(5,5,"Population: " + str(len(self.population)),7)
        pyxel.text(5,10,"Food: " + str(len(self.food)),7)
        pyxel.text(5,15,"Average Fitness: " + str(calcPop(self.population,"fitness")),7)
        pyxel.text(5,20,"Tick Number: " + str(self.tick_num),7)
        pyxel.text(5,25,"Generation Number: " + str(self.generation_num),7)