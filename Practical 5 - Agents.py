# Additional parts added:
# - Protect self.x and self.y
# - Implement property attribute for these, with appropriate get and set\
# methods

import random
import operator
import matplotlib.pyplot
import agentframework1

# Create a function which calculates the distance between all sets of 2 points.
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

'''
# Check that this file is reading agentframework1 file
a = agentframework1.Agent()
print(a.y, a.x)
# Check that this file is reading move function given in angentframework1 file
a.move()
print(a.y, a.x)
'''

# Defines the number of agents and iterations and creates an empty coordinates
# list for agents.
    
num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework1.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

# Plot the agents.   
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# Run distance_between function between pairs of agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
<<<<<<< HEAD
        
=======
>>>>>>> a6696f2a5ede0eaddc0c196d77239414bc21e159
