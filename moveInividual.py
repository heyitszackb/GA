import random
import math

def moveIndividualRandom():
    pass

def moveIndividual(individual, width, height, closestFood):
    
    creatureX,creatureY = individual.getCoords()
    if closestFood:
        foodX,foodY = closestFood.getCoords()
        currentX = foodX - creatureX
        currentY = foodY - creatureY
        newX = individual.scale[0] * currentX
        newY = individual.scale[1] * currentY

        if individual.energy > 0:
            
            newD = math.sqrt(newX**2 + newY**2)
            if newD != 0:

                angleA = math.asin(newY/newD)
                angleB = math.asin(newX/newD)
                moveX = math.sin(angleB) * individual.speed
                moveY = math.sin(angleA) * individual.speed

                if (creatureX + moveX < width) and (creatureY + moveY < height) and \
                (creatureX + moveX > 0) and (creatureY + moveY > 0) and \
                individual.energy > 0 and newD != 0:
                    # print("here!")
                    # print("moveX:",moveX)
                    # print("moveY:",moveY)
                    # print("energy:",individual.energy)
                    individual.setCoords(creatureX + moveX, creatureY + moveY)
                    individual.energy -= 1
                    return individual
            
    updateX = random.randint(-(individual.speed),(individual.speed))
    updateY = random.randint(-(individual.speed),(individual.speed))
    if (creatureX + updateX < width) and (creatureY + updateY < height) and \
    (creatureX + updateX > 0) and (creatureY + updateY > 0) and (individual.energy > 0):
        individual.setCoords(creatureX+updateX,creatureY+updateY)
        individual.energy -= 1

    return individual

"""
1. get x,y of closest food
2. calculate newX,newY
3. account for speed (use sin(A))
"""