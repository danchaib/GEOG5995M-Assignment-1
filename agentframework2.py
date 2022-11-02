import random

class Agent():
    def __init__(self, environment, agents):
        self._x = random.randint(0,99) 
        self._y = random.randint(0,99) 
        self.environment = environment
        self.agents = agents
        self.store = 0
        
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
            
# If environment has value 10 or higher, agent eats values of 10.
# If environment has values less than 10, agent eats that exact value.
    def eat(self): 
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
        for i in range(1, 9):
            if self.environment[self.y][self.x] < 10:
                self.environment[self.y][self.x] -= i
                self.store += i  
            
# If store of an agent is greater than 100, agent drops store.
    def drop(self):
        if self.store > 100:
            self.environment[self.y][self.x] = self.environment[self.y][self.x] + self.store
            self.store = 0
            
# If distance between agents is less than neighbourhood, store is shared.        
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
        
# When printed each agent for each iteration, gives agents coordinates and store.
    def __str__(self):
        print(self._y, self._x, self.store)        
        
# Defines distance between pairs of agents.            
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 

        # Creates docstrings for x and y attributes.
    x = property(getx, setx, "I'm the 'x' property.")       
    y = property(gety, sety, "I'm the 'y' property.") 