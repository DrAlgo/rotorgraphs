from rotorgraphs import *

g = nx.MultiDiGraph([[1,2],[1,2],[1,3],[2,3]])
print(list(g.out_edges(1)))