import random

class Agent():
    def __init__(self):
        self._x = random.randint(0,99) 
        self._y = random.randint(0,99) 
        
# Functions to set and get x and y values.
    def setx(self, value):
        self._x = value
        
    def sety(self, value):
        self._y = value      
    
    def getx(self):
        return self._x
    
    def gety(self):
        return self._y
    
# Moves agents 1 space in x and y-directions.
# Random number generator dictates directions of movement in x and y.
    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
            
        # Creates docstrings for x and y attributes.
    x = property(getx, setx, "I'm the 'x' property.")       
    y = property(gety, sety, "I'm the 'y' property.") 