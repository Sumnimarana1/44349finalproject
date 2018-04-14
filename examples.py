# Class: 44-349 A Survey of Algorithms
# Author: Anthony Enriquez, Sumnima Rana, David Schmitt
# Description: Final Project
# Due: 4/20/18
# We pledge that we have completed the programming assignment independently.
# We have not copied the code from a student or any source.
# We have not given my code to any other student.
# We have not given my code to any other student and will not share this code with anyone under any circumstances.

from graphcoloring import regcolor, schedule
import networkx as nx

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
             ('E','H'), ('F','G'),  ('G','H')]
G2.add_nodes_from(nodelist2)
G2.add_edges_from(edgelist2)

regcolor(G)
regcolor(G2)