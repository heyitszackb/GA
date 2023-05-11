from Const import CREATURE_INITIAL_ENERGY

class Creature:
    def __init__(self, size, speed, scale, sense):
        self.size = size
        self.speed = speed
        self.energy = CREATURE_INITIAL_ENERGY
        self.x = 0
        self.y = 0
        self.sense = sense
        self.scale = scale # [gx,gy]
        self.closestFood = None
    
    
    def getFitness(self):
        return self.energy

    def setSize(self,newSize):
        self.size = newSize
    
    def getSize(self):
        return self.size

    def setCoords(self,x,y):
        self.x = x
        self.y = y
    
    def getCoords(self):
        return self.x,self.y