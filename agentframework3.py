# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:28:15 2022

@author: Dan Chaib
"""
import random

class Agent():
    """
    Class used to provide functionality to agents interacting
    in environment, as well as protecting x and y coordinate values.
    """
    def __init__(self, environment, agents):
        """
        Used to initialise agents into the environment.
        
        Parameters
        ----------
        environment : List
            A list of integer values used to form an environment.
        agents : List
            A list of all 'agents'.
        Returns
        -------
        None.
        """
        self._x = random.randint(0,99) 
        self._y = random.randint(0,99) 
        self.environment = environment
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
        Number (Integer)
            self._x
        
        """
        return self._x
    
    def gety(self):
        """
        Retrieves x attribute value.

        Returns
        -------
        Number (Integer)
            self._y

        """
        return self._y
    
# Moves agents 1 space in x and y-directions.
# Random number generator dictates directions of movement in x and y.
    def move(self):
        """
        Function which moves 'agents' by changing their x and y-
        coordinates.

        Returns
        -------
        None.

        """
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
        """
        Function allowing for 'agents' to eat the environment.

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
        Function allowing for 'agents' to drop 'food' onto the
        environment.

        Returns
        -------
        None.

        """
        if self.store > 100:
            self.environment[self.y][self.x] = self.environment[self.y][self.x] + self.store
            self.store = 0
            
# If distance between agents is less than neighbourhood, store is shared.        
    def share_with_neighbours(self, neighbourhood):
        """
        Function for nearby 'agents' to share food.

        Parameters
        ----------
        neighbourhood : Number (Integer)
            Value of distance between 'agents' within which they share
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
                #print("sharing " + str(dist) + " " + str(ave))
        
# When printed each agent for each iteration, gives agents coordinates and store.
    def __str__(self):
        """
        Gives the y-coordinate, x-coordinate and store values of 'agents'.

        Returns
        -------
        None.

        """
        print(self._y, self._x, self.store)        
        
# Defines distance between pairs of agents.            
    def distance_between(self, agent):
        """
        Function to measure distance between two 'agents' (self and agent).

        Parameters
        ----------
        agent : List
            Singular agent from agents.

        Returns
        -------
        Number (Float)
            Represents the distance between two 'agents'.

        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 

        # Creates docstrings for x and y attributes.
    x = property(getx, setx, "I'm the 'x' property.")       
    y = property(gety, sety, "I'm the 'y' property.") 