# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:28:15 2022

@author: Dan Chaib
"""
# Additional parts added:
# - Make nibblers change behaviour based on their store. 
# - This was done in the form of agents with a store of >= 50 moving length 5\
# - and agents with a store of <50 moving length 1
# - Wolves were added, changing their graph symbol to a cross
# - Sheep breeding and wolves killing sheep was attempted however not\
# - successful code for these two functions was left in only for formative\
# - feedback and not for marking purposes.

import random
import operator
import matplotlib.pyplot as plt
import matplotlib.animation 
import agentframeworknew
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

'''
# Create a function which calculates the distance between all sets of 2 points.
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5
'''

# Defines the number of agents and iterations and creates an empty coordinates
# list for agents.
num_of_agents = 10
num_of_wolves = 10
num_of_iterations = 1000
neighbourhood = 20
agents = []
wolves = []

# For animation.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframeworknew.Agent(environment, agents, wolves))

# Make the wolves.
for i in range(num_of_wolves):
    wolves.append(agentframeworknew.Agent(environment, agents, wolves))    

# For stopping function.
carry_on = True

# Agents move, eat, share, drop, and print location and store information.
# Agents are shuffled into a random order before each iteration of events.    
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    random.shuffle(agents) 
    
    for i in range(num_of_agents):
        
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood) 
        agents[i].drop()
        agents[i].breed_sheep(neighbourhood, agents, wolves, environment)
        agents[i].__str__()
        
    for i in range(num_of_wolves):
        
        wolves[i].move()
        wolves[i].kill_sheep(neighbourhood, agents, wolves, environment)
        wolves[i].__str__()

    # Stopping Condition - Random
    
#    if random.random() < 0.1:
#        carry_on = False
#        print("stopping condition")

    # Stoppng Conditon - All Agents Store > 20
    count = 0
    for i in range(num_of_agents):
        if agents[i].store > 50:
            count = count + 1
    if count == len(agents):
        print ("Stopping Condition", frame_number + 1)
        carry_on = False
    
# Plot the agents and wolves in the environment.   
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i].x,agents[i].y, "sheep")
        plt.text(agents[i].x,agents[i].y, "sheep")
    for i in range(num_of_wolves):
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, marker = 'X')
        print(wolves[i].x,wolves[i].y, "wolf")
        plt.text(wolves[i].x,wolves[i].y, "wolf")
    matplotlib.pyplot.show()
    
# For generating stopping condition.
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

animation = matplotlib.animation.FuncAnimation\
(fig, update, interval=1, repeat=False, frames=gen_function)

matplotlib.pyplot.show()

'''
# Run distance_between function between pairs of agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 
'''

# Write out the environment as new file.
updatedenv = open('updatedenv.csv', 'w', newline='')
writer = csv.writer(updatedenv, delimiter=' ')
for row in environment:
    writer.writerow(row)
updatedenv.close()



