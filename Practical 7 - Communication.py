# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:28:15 2022

@author: Dan Chaib
"""
# No additional parts added to this practical

import random
import operator
import matplotlib.pyplot
import agentframework3
import csv

# Opens in.txt file and reads the csv into the environment list 
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in reader:
        rowlist = [] 
        for value in row:
            rowlist.append(value)
            #print(value) 
        environment.append(rowlist)

# Create a function which calculates the distance between all sets of 2 points.
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Defines the number of agents and iterations and creates an empty coordinates
# list for agents.
    
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework3.Agent(environment, agents))

# Agents move, eat, share, drop, and print location and store information.
# Agents are shuffled into a random order before each iteration of events.    
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        # print(neighbourhood)
        agents[i].drop()
        agents[i].__str__()

# Plot the agents in the environment.   
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# Run distance_between function between pairs of agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 

# Write out the environment as new file.
updatedenv = open('updatedenv.csv', 'w', newline='')
writer = csv.writer(updatedenv, delimiter=' ')
for row in environment:
    writer.writerow(row)
updatedenv.close()




