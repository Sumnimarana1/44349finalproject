# Class: 44-349 A Survey of Algorithms
# Author: Anthony Enriquez, Sumnima Rana, David Schmitt
# Description: Final Project
# Due: 4/20/18
# We pledge that we have completed the programming assignment independently.
# We have not copied the code from a student or any source.
# We have not given my code to any other student.
# We have not given my code to any other student and will not share this code with anyone under any circumstances.

import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter



def color(G):
    # sort nodes by degree, dec value (value,deg)
    sortednodes = sorted(G.degree, key=itemgetter(1), reverse=True)
    newnodelist = [a[0] for a in sortednodes]

    G2 = nx.Graph();
    G2.add_nodes_from(newnodelist, color='null')
    G2.add_edges_from(G.edges)

    print(newnodelist[0])

    #print(G2.node[newnodelist[0]]['color'])
    for node in newnodelist[1:]:
        print(G2.nodes[node])
    return G2


def draw(G):
    # Position nodes using Fruchterman-Reingold force-directed algorithm
    pos = nx.spring_layout(G)
    colors = ['blue', 'red', 'yellow', 'green', 'orange', 'purple']
    # draw graph and us matplotlib to visualize
    nx.draw(G, pos, with_labels=True, node_color= colors)

# test

# init graph
G = nx.Graph()

# create list of nodes, edges and add to G
nodelist = ['A', 'B', 'C', 'D', 'E', 'F']
edgelist = [('A','B'),('B','C'),('B','D'), ('C', 'D'), ('C', 'E'), ('C', 'F')]
G.add_nodes_from(nodelist)
G.add_edges_from(edgelist)

coloredgraph = color(G)
draw(coloredgraph)
plt.show()