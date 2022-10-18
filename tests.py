from rotorgraphs import *

g = nx.MultiDiGraph([[1,2],[1,2],[1,3],[2,3]])
for v in g.nodes:
        g.nodes[v]['sink'] = False
#print(g.nodes[1]['sink'])

r = standard_rotor_config(g)
print(r)
turn(g,1, r)
print(r)
turn(g,1, r)
print(r)
turn(g,1, r)
print(r)