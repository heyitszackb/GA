from Food import Food
import random
from Creature import Creature
from Const import INITIAL_SIZE_LOWER_BOUND, INITIAL_SIZE_UPPER_BOUND, \
    INITIAL_SPEED_LOWER_BOUND, INITIAL_SPEED_UPPER_BOUND, MAX_FOOD_ON_SCREEN, \
        INITIAL_SENSE_LOWER_BOUND, INITIAL_SENSE_UPPER_BOUND

def initPopCoords(population,width,height):
    for i in range(len(population)):
        x = random.randint(0,width)
        y = random.randint(0,height)
        population[i].setCoords(x,y)
    return population


def initFoods(width,height):
    food = []
    for i in range(MAX_FOOD_ON_SCREEN):
        x = random.randint(0,width)
        y = random.randint(0,height)
        f = Food()
        f.setCoords(x,y)
        food.append(f)
    return food


def initPopulation(population_size):
    population = []
    for _ in range(population_size):
        scale = [round(random.uniform(-1,1),2), round(random.uniform(-1,1),2)]
        sense = random.randint(INITIAL_SENSE_LOWER_BOUND, INITIAL_SENSE_UPPER_BOUND)
       
        population.append(Creature(random.randint(INITIAL_SIZE_LOWER_BOUND, INITIAL_SIZE_UPPER_BOUND),
                                   random.randint(INITIAL_SPEED_LOWER_BOUND, INITIAL_SPEED_UPPER_BOUND),
                                   scale,
                                   sense
                                   ))
    return population