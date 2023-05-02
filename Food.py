from Const import INITIAL_ENERGY_FROM_FOOD, FOOD_SIZE

class Food:
    def __init__(self):
        self.size = FOOD_SIZE
        self.energy = INITIAL_ENERGY_FROM_FOOD
        self.x = 0
        self.y = 0

    def setCoords(self,x,y):
        self.x = x
        self.y = y

    def getSize(self):
        return self.size

    def getCoords(self):
        return self.x,self.y