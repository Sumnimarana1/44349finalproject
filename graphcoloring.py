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

colorlist = ['red', 'green', 'blue', 'magenta', 'yellow', 'orange', 'lime', 'cyan', 'purple', 'brown', 'pink', 'grey']

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
        value = next(index for index,value in enumerate(available) if value == True)
        G.nodes[node].update({'color' : value})

# draw graph
def draw(G):
    # Position nodes using Fruchterman-Reingold force-directed algorithm
    pos = nx.spring_layout(G)

    # fetch colors from graph, map to actual color, then store in colors array
    colors =[]
    for node in G.nodes:
        colors.append(colorlist[G.node[node]['color']])

    # draw graph and us matplotlib to visualize
    nx.draw(G, pos, with_labels=True, node_color= colors)

# display graph information Node, atr, color, χ(G), bipartite, planer, returns χ(G)
def info(G, atrs):
    print('Node\tAttribute\t"Color"')
    print("---------------------------")

    for node in G.nodes:
        print('{:<14}{:12}{}'.format(node, atrs[G.node[node]['color']], G.node[node]['color']))

    print("---------------------------")
    chromaticnum = max(nx.get_node_attributes(G,'color').values()) + 1
    print("χ(G): {}".format(chromaticnum))

    if chromaticnum <= 4:
        if chromaticnum <= 2:
            print("Graph is bipartite")
        print("Graph is planer")

    print()

    return chromaticnum

# normal coloring
def regcolor(G):
    color(G)
    draw(G)
    info(G,colorlist)
    plt.show()

# use graph coloring to resolve scheduling conflicts
def schedule(G,atrs):
    color(G)
    draw(G)
    info(G,atrs)
    plt.show()