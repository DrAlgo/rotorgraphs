from generators import *
from rotorgraphs import *

"""
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

sigma = {v:0 for v in g.nodes}
print('s',sigma)
a = list(g.edges(1))[0]
move(sigma, a)
print('s',sigma)
"""

g = standard_binary_path(5)
rho = sbp_configuration('RRLLL')
print(rho)
rout_single_particle(g, rho, 3)
print(rho)
