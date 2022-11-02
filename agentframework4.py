# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:28:15 2022

@author: Dan Chaib
"""
import random

class Agent():
    """
    Class used to provide functionality to agents and wolves interacting
    in environment, as well as protecting x and y coordinate values.
    """
    def __init__(self, environment, agents, wolves):
        """
        Used to initialise agents and wolves into the environment.
        
        Parameters
        ----------
        environment : List
            A list of integer values used to form an environment.
        agents : List
            A list of all 'agents', sometimes referred to as 'sheep'.
        wolves : List
            A list of all 'wolves'
        y : Number (Integer)
            y-coordinate of each agent and wolf. The default is None.
        x : Number (Integer)
            y-coordinate of each agent and wolf. The default is None.

        Returns
        -------
        None.
        """
        self._x = random.randint(0,99) 
        self._y = random.randint(0,99) 
        self.environment = environment
        self.wolves = wolves
        self.agents = agents
        self.store = 0
        
# Functions to set and get x and y values.
    def setx(self, value):
        """
        Sets x attribute value.

        Parameters
        ----------
        value : Number (Integer)

        Returns
        -------
        None.

        """
        self._x = value
        
    def sety(self, value):
        """
        Sets y attribute value.

        Parameters
        ----------
        value : Number (Integer)

        Returns
        -------
        None.

        """
        self._y = value      
    
    def getx(self):
        """
        Retrieves x attribute value.

        Returns
        -------
        Number (Float)    
            self._x

        
        """
        return self._x
    
    def gety(self):
        """
        Retrieves x attribute value.

        Returns
        -------
        Number (Float)    
            self._y


        """
        return self._y

# Function moving agent, if store is greater agent moves more spaces (more energy).
# In addition, random number condition dictating direction of travel.
    def move(self):
        """
        Function which moves agents and wolves by changing their x and y-
        coordinates.

        Returns
        -------
        None.

        """
        if random.random() < 0.5:
            if self.store <= 50:
                self._x = (self._x + 1) % 100
            else:
                self._x = (self._x - 1) % 100
                    
            if self.store <= 50:
                self._y = (self._y + 1) % 100
            else:
                self._y = (self._y - 1) % 100 
                
            if self.store > 50:
                self._x = (self._x + 5) % 100
            else:
                self._x = (self._x - 5) % 100
            
            if self.store > 50:
                self._y = (self._y + 5) % 100
            else:
                self._y = (self._y - 5) % 100     


# Function moving agent, dependent on value of randomly generated number.
#    def move(self):
#        if random.random() < 0.5:
#            self._x = (self._x + 1) % 100
#        else:
#            self._x = (self._x - 1) % 100
#
#        if random.random() < 0.5:
#            self._y = (self._y + 1) % 100
#        else:
#            self._y = (self._y - 1) % 100 

# If environment has value 10 or higher, agent eats values of 10.
# If environment has values less than 10, agent eats that exact value.
    def eat(self): 
        """
        Function allowing for 'agents/sheep' to eat the environment.

        Returns
        -------
        None.

        """
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
        for i in range(1, 9):
            if self.environment[self.y][self.x] < 10:
                self.environment[self.y][self.x] -= i
                self.store += i 
            
# If store of an agent is greater than 100, agent drops store.
    def drop(self):
        """
        Function allowing for 'agents/sheep' to drop 'food' onto the
        environment.

        Returns
        -------
        None.

        """
        if self.store > 100:
            self.environment[self.y][self.x] = \
            self.environment[self.y][self.x] + self.store
            self.store = 0
        
# When printed each agent for each iteration, gives agents coordinates and store.
    def __str__(self):
        """
        Gives the y-coordinate, x-coordinate and store values of 'agents' and 
        'wolves'.

        Returns
        -------
        None.

        """
        print(self._y, self._x, self.store)
        
# If distance between agents is less than neighbourhood, store is shared.        
    def share_with_neighbours(self, neighbourhood):
        """
        Function for nearby 'agents/sheep' to share food.

        Parameters
        ----------
        neighbourhood : Number (Integer)
            Value of distance between 'agents/sheep' within which they share
            food.

        Returns
        -------
        None.

        """
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
      
# BREED_SHEEP AND KILL_SHEEP DON'T WORK, I'VE ONLY LEFT THEM IN FOR FORMATIVE \
# FEEDBACK.
    
#    def breed_sheep(self, neighbourhood, agent, wolves, environment):
#       for agent in self.agents:
#           distance = self.distance_between(agent)
#           if distance <= neighbourhood:
#              self.agents.append(Agent(environment, agent, wolves))           
#              
#                             
#    def kill_sheep(self, neighbourhood, agents, wolves, environment):
#       for wolf in self.wolves:
#           for agent in self.agents:
#               distance = self.distance_between(wolf)
#               if distance <= neighbourhood:
#                   wolf.store = agent.store
#                   self.agents.remove(Agent(environment, agent, wolves))
                
# Defines distance between pairs of agents.            
    def distance_between(self, agent):
        """
        Function to measure distance between two agents (self and agent).

        Parameters
        ----------
        agent : List
            Singular agent from agents.

        Returns
        -------
        Number (Float)
            Represents the distance between two agents.

        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 

# Creates docstrings for x and y attributes.
    x = property(getx, setx, "I'm the 'x' property.")       
    y = property(gety, sety, "I'm the 'y' property.") 