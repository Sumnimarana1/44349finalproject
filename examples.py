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

# Graph 1: Simple example
# init graph
G = nx.Graph()

# create list of nodes, edges and add to G
nodelistg1 = ['A', 'B', 'C', 'D', 'E', 'F']
edgelistg1 = [('A','B'),('B','C'),('B','D'), ('C', 'D'), ('C', 'E'), ('C', 'F')]
G.add_nodes_from(nodelistg1)
G.add_edges_from(edgelistg1)

# Graph 2: Complete Graph w/ 8 nodes
G2 = nx.complete_graph(8)

# Graph 3: Bipartite
G3 = nx.Graph()
nodelistg3 = ['A', 'B', 'C', 'D', 'E']
edgelistg3 = [('A','C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B','D'), ('B', 'E')]
G3.add_nodes_from(nodelistg3)
G3.add_edges_from(edgelistg3)

# Graph 4: Florentine families
G4 = nx.florentine_families_graph()

# Graph 5: Random Regular graph w 100 nodes, each w/ degree 12
G5 = nx.random_regular_graph(12,100, seed=None)

# Graph 6: Assembly process w/ 6 distinct steps
# Each step takes 5 mins
# No two steps of A, B, and E may be done at the same time
# Steps B and D may not be done at the same time
# No two of steps C, D, and F may be done at the same time
G6 = nx.Graph()
nodelistg5 = ['A', 'B', 'C', 'D', 'E', 'F']
edgelistg5 = [('A', 'B'), ('A', 'E'), ('B', 'E'), ('B', 'D'), ('C', 'D'), ('C', 'F'), ('D', 'F')]
phaselist = ['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4', 'Phase 5', 'Phase 6']
G6.add_nodes_from(nodelistg5)
G6.add_edges_from(edgelistg5)

# Graph 7: Final Exam Schedule
# Schedule the final exams for Math 115, Math 116, Math 185, Math 195, CS 101, CS 102, CS 273, and CS 473,
# using the fewest number of different time slots, if there are no students taking both Math 115 and CS 473,
# both Math 116 and CS 473, both Math 195 and CS 101, both Math 195 and CS 102, both Math 115 and Math 116,
# both Math 115 and Math 185, and both Math 185 and Math 195, but there are students in every other pair of courses.
G7 = nx.Graph()
nodelistg6 = ['Math 115', 'Math 116', 'Math 185', 'Math 195', 'CS 101', 'CS 102', 'CS 273', 'CS 473']
edgelistg6 = [('Math 115', 'Math 195'), ('Math 115', 'CS 101'), ('Math 115', 'CS 102'), ('Math 115', 'CS 273'),
              ('Math 116', 'Math 185'), ('Math 116', 'Math 195'), ('Math 116', 'CS 101'), ('Math 116', 'CS 102'),
              ('Math 116', 'CS 273'), ('Math 185', 'CS 101'), ('Math 185', 'CS 102'), ('Math 185', 'CS 273'),
              ('Math 185', 'CS 473'), ('Math 195', 'CS 273'), ('Math 195', 'CS 473'), ('CS 101', 'CS 102'),
              ('CS 101', 'CS 273'), ('CS 101', 'CS 473'), ('CS 102', 'CS 273'), ('CS 102', 'CS 473'),
              ('CS 273', 'CS 473')]
periodlist = ['Period 1', 'Period 2', 'Period 3', 'Period 4', 'Period 5', 'Period 6', 'Period 7', 'Period 8']
G7.add_nodes_from(nodelistg6)
G7.add_edges_from(edgelistg6)

# use our methods to find graph coloring :)
print("Graph 1: Simple example")
regcolor(G)
print("Graph 2: Complete Graph w/ 8 nodes")
regcolor(G2)
print("Graph 3: Bipartite")
regcolor(G3)
print("Graph 4: Florentine families")
regcolor(G4)
print("Graph 5: Random Regular graph w 100 nodes, each w/ degree 12")
regcolor(G5)
print("Graph 6: Assembly process w/ 6 distinct steps")
schedule(G6, phaselist)
print("Graph 7: Final Exam Schedule")
schedule(G7, periodlist)