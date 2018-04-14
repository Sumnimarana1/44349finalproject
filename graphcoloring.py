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

    # create new graph w/ sorted nodes
    G2 = nx.Graph()
    G2.add_nodes_from(newnodelist)
    G2.add_edges_from(G.edges)

    colorlist = ['r', 'g', 'b', 'm', 'yellow', 'orange', 'lime', 'cyan', 'purple', 'brown', 'pink', 'grey']

    # set init color for node w/ highest degree
    G2.nodes[newnodelist[0]].update({'color': colorlist[0]})

    available = [False for value in range(len(colorlist))]

    for node in newnodelist[1:]:
        for adj in G2.neighbors(node):
            if ('color' in G2[adj]) == True:
                print("Node" + node)
                print("is false")

            #print('color' in G2[adj])


    '''i = 1
    for node in newnodelist[1:]:
        G2.nodes[node].update({'color' : colorlist[i]})
        print(G2.nodes[node])
        i += 1'''

    print(nx.get_node_attributes(G2, 'color'))
    # print(G2.nodes['C'])

    return G2


def draw(G):
    # Position nodes using Fruchterman-Reingold force-directed algorithm
    pos = nx.spring_layout(G)

    # fetch colors from graph and store in colors array
    colors = []
    atr = nx.get_node_attributes(G, 'color')
    for nodes in G.nodes:
        colors.append(atr[nodes])

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
#draw(coloredgraph)
#plt.show()