# Class: 44-349 A Survey of Algorithms
# Author: Anthony Enriquez, Sumnima Rana, David Schmitt
# Description: Final Project
# Due: 4/20/18
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any other student.
# I have not given my code to any other student and will not share this code with anyone under any circumstances.

import networkx as nx
from networkx_viewer import Viewer

G = nx.MultiDiGraph()
G.add_edge('Arg2','Arg1')
G.add_edge('Arg3','Arg1',0)
G.add_edge('Arg3','Arg1',1)
G.add_edge('Arg4','Arg2')
G.add_edge('Arg5','Arg2')
G.add_edge('Arg6','Arg3')
G.node['Arg2']['outline'] = 'blue'
G.node['Arg1']['label_fill'] = 'red'
app = Viewer(G)
app.mainloop()