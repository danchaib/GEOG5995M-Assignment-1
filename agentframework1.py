# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:28:15 2022

@author: Dan Chaib
"""
import random

class Agent():
    """
    Class used to provide functionality to agents 
    as well as protecting x and y coordinate values.
    """
    def __init__(self):
        """
        Used to initialise agents by setting start coordinates.

        Returns
        -------
        None.
        """
        self._x = random.randint(0,99) 
        self._y = random.randint(0,99) 
        
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
    
# Moves agents 1 space in x and y-directions.
# Random number generator dictates directions of movement in x and y.
    def move(self):
        """
        Function which moves agents and wolves by changing their x and y-
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
            
        # Creates docstrings for x and y attributes.
    x = property(getx, setx, "I'm the 'x' property.")       
    y = property(gety, sety, "I'm the 'y' property.") 