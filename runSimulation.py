from initialize import initPopCoords, initFoods
from spawnFood import spawnFood
from updatePopulation import updatePopulation

def runSimulation(population,ticks, width, height):
    # PROBLEM LIST:
    # we could probably optimize this whole thing somehow
    # Food spawning on top of dead creatures
    # What to do with dead creatures?
    population = initPopCoords(population,width,height)
    food = initFoods(width,height)

    for _ in range(ticks):
        population,food = updatePopulation(population,food,width,height)
        food = spawnFood(food,width,height)

    return population