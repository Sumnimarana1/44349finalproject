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

# color graph using greedy algo (welsh-powell)
def color(G):
    # sort nodes by degree, dec value (value,deg)
    sortednodes = sorted(G.degree, key=itemgetter(1), reverse=True)
    newnodelist = [a[0] for a in sortednodes]

    # set init color for node w/ highest degree
    G.nodes[newnodelist[0]].update({'color' : 0})

    # iterate over rest of nodes in dec degree order
    for node in newnodelist[1:]:
        available = [True for value in range(len(newnodelist))]     # temp array to find available color

        # check adj nodes for color, if they do, make color false in temp array
        for adj in G.neighbors(node):
            if ('color' in G.nodes[adj]) == True:
                available[G.node[adj]['color']] = False

        # assign first available color
        value = next(i for i,v in enumerate(available) if v == True)
        G.nodes[node].update({'color' : value})

    return G


def draw(G):
    # Position nodes using Fruchterman-Reingold force-directed algorithm
    pos = nx.spring_layout(G)

    # fetch colors from graph and store in colors array
    colorlist = ['r', 'g', 'b', 'm', 'yellow', 'orange', 'lime', 'cyan', 'purple', 'brown', 'pink', 'grey']
    colors =[]
    atr = nx.get_node_attributes(G, 'color')
    for nodes in G.nodes:
        colors.append(colorlist[atr[nodes]])

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

G2 = nx.Graph()
nodelist2 = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
edgelist2 = [('A','B'), ('A','C'),  ('B','D'), ('B','E'), ('C','D'), ('C','H'), ('D','E'), ('D','F'), ('D','G'),
             ('D', 'H'), ('E','H'), ('F','G'),  ('G','H'),]
G2.add_nodes_from(nodelist2)
G2.add_edges_from(edgelist2)

coloredgraph = color(G)
coloredgraph2 = color(G2)
print(nx.get_node_attributes(G, 'color'))
draw(coloredgraph)
plt.show()
draw(coloredgraph2)
plt.show()