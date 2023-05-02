from moveInividual import moveIndividual
import math
import pyxel

def updatePopulation(population,food,width,height):
    for i in range(len(population)):
        # if the individual is alive
        if population[i].energy > 0:
                
            creatureX,creatureY = population[i].getCoords()
            closestFood = None
            closestFoodDistance = 10000000
            for j in range(len(food)):
                # secretly get the closest food item and store it in the creature

                if food[j] == None:
                    continue
                foodX,foodY = food[j].getCoords()
                # distance = math.sqrt((creatureX - foodX)**2 + (creatureY - foodY)**2)
                distance = abs(creatureX - foodX) + abs(creatureY - foodY)

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



# from scipy.spatial import cKDTree
# import pyxel

# def updatePopulation(population, food, width, height):
#     # create a KD tree with the coordinates of the food
#     food_coords = [food_item.getCoords() for food_item in food if food_item is not None]
#     tree = cKDTree(food_coords)
        
#     for creature in population:
#         # if the individual is alive
#         if creature.energy > 0:
#             creature_x, creature_y = creature.getCoords()
#             closest_food_distance, closest_food_index = tree.query((creature_x, creature_y), distance_upper_bound=creature.sense)
#             if closest_food_distance == float('inf'):
#                 # no food was found within the creature's sense range
#                 closest_food = None
#                 moveIndividual(creature, width, height, closest_food)
#             else:
#                 # get the food item with the closest distance
#                 closest_food = food[closest_food_index]
#                 if closest_food is None:
#                     # the food item was already consumed by another creature
#                     continue
            
#                 if closest_food_distance <= ((creature.getSize()) + (closest_food.getSize())):
#                     # the creature is overlapping with the food item
#                     creature.energy += closest_food.energy
#                     food[closest_food_index] = None
#                 else:
#                     # move the creature towards the closest food item
#                     creature.closestFood = closest_food
#                     moveIndividual(creature, width, height, closest_food)
    
#     # remove the consumed food items
#     clean_foods = [food_item for food_item in food if food_item is not None]
    
#     return population, clean_foods