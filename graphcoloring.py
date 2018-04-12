# Class: 44-349 A Survey of Algorithms
# Author: Anthony Enriquez, Sumnima Rana, David Schmitt
# Description: Final Project
# Due: 4/20/18
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any other student.
# I have not given my code to any other student and will not share this code with anyone under any circumstances.

import networkx as nx
import matplotlib.pyplot as plt



G = nx.Graph()

G.add_edge(1, 2)
G.add_edge(2,3)
pos = nx.spring_layout(G)

nx.draw(G,pos)
plt.show()
