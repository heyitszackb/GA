from Const import CREATURE_INITIAL_ENERGY, INITIAL_SENSE_LOWER_BOUND, INITIAL_SENSE_UPPER_BOUND, INITIAL_SPEED_LOWER_BOUND, INITIAL_SPEED_UPPER_BOUND
import pyxel

class Creature:
    def __init__(self, size, speed, scale, sense):
        self.energy = CREATURE_INITIAL_ENERGY

        # Variables
        self.closestFood = None
        self.is_best_individual = False
        self.x = 0
        self.y = 0

        # Genes
        scaledSpeed = (speed - INITIAL_SPEED_LOWER_BOUND) / (INITIAL_SPEED_UPPER_BOUND-INITIAL_SPEED_LOWER_BOUND)
        scaledSense = (sense - INITIAL_SENSE_LOWER_BOUND) / (INITIAL_SENSE_UPPER_BOUND-INITIAL_SENSE_LOWER_BOUND)
        tmpScaledSpeed = scaledSpeed - scaledSense if scaledSpeed - scaledSense > 0 else 0
        scaledSense = scaledSense - scaledSpeed if scaledSense - scaledSpeed > 0 else 0
        self.speed = int((tmpScaledSpeed * (INITIAL_SPEED_UPPER_BOUND - INITIAL_SPEED_LOWER_BOUND)) + INITIAL_SPEED_LOWER_BOUND)
        self.sense = int((scaledSense * (INITIAL_SENSE_UPPER_BOUND - INITIAL_SENSE_LOWER_BOUND)) + INITIAL_SENSE_LOWER_BOUND)
        self.size = size
        self.scale = scale # [gx,gy]
         
         # Maybe we switch scaledSpeed and scaledSense orders in subtraction?
         # maybe we need to penalize a bigger sense range more?
    def draw(self):
        if self.energy > 0:
            if self.is_best_individual:
                pyxel.circ(self.x,self.y,self.size,11)
                pyxel.circb(self.x,self.y,self.sense,11)
            else:
                pyxel.circ(self.x,self.y,self.size,7)
                pyxel.circb(self.x,self.y,self.sense,4)
    
    
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