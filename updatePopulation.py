from moveInividual import moveIndividual
import math

def updatePopulation(population,food,width,height):
    for i in range(len(population)):
        
        creatureX,creatureY = population[i].getCoords()
        closestFood = None
        closestFoodDistance = 10000000
        for j in range(len(food)):
            # secretly get the closest food item and store it in the creature

            if food[j] == None:
                continue
            foodX,foodY = food[j].getCoords()
            distance = math.sqrt((creatureX - foodX)**2 + (creatureY - foodY)**2)

            # see if we are overlapping with the food
            if distance <= ((population[i].getSize()) + (food[j].getSize())):
                population[i].energy += food[j].energy
                food[j] = None
                continue
                
            # try to find the closest food
            if (distance < closestFoodDistance) and (distance < population[i].sense):
                closestFood = food[j]
                closestFoodDistance = distance
            
        population[i].closestFood = closestFood
        moveIndividual(population[i],width,height,closestFood)
    clean_foods = []
    # print("FOOD",food)
    for i in range(len(food)):
        if food[i] != None:
            clean_foods.append(food[i])
    # print("CLEAN FOOD",clean_foods)
    return population,clean_foods