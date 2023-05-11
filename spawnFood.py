import random
from Food import Food

from Const import MAX_FOOD_ON_SCREEN, CHANCE_FOR_FOOD_TO_SPAWN_AT_TICK, NUM_FOOD_TO_SPAWN_AT_TICK

def spawnFood(food,width,height):

    num = random.random()
    for i in range(NUM_FOOD_TO_SPAWN_AT_TICK):
        if num < CHANCE_FOR_FOOD_TO_SPAWN_AT_TICK and len(food) < MAX_FOOD_ON_SCREEN:
            x = random.randint(0,width)
            y = random.randint(0,height)
            f = Food()
            f.setCoords(x,y)
            food.append(f)
    return food