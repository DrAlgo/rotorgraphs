import networkx as nx
import copy



def graphToMultiDigraph(g):
    """
    takes an undirected graph and returns a multi directed graph
    with two arcs for each previous edge
    """
    res = nx.MultiDiGraph()
    res.add_nodes_from(copy.deepcopy(g.nodes))

    for v in res.nodes:
        res.nodes[v]['sink'] = False

    edges = copy.deepcopy(g.edges)
    for a,b in edges:
        res.add_edge(a,b)
        res.add_edge(b,a)
    return res

"""
this is intended to work with nx.MultiDiGraph
A rotor configuration is a dict {node:edge}
the rotor order on a node a is the order in the dict g[a]

each node should contain a property "sink" set to True of False
"""



def standard_rotor_config(g):
    """returns a rotor configuration
    with the first stored arc for every vertex"""
    return {v : next(iter(g.neighbors(v))) for v in h.nodes }

def non_sink_nodes(g):
    return (v for v in g.nodes(data=True) if v['sink']==False)

def standard_binary_path(n):
    """
    returns the standard binary path rotor graph on n non_sink vertices 1, 2, ..., n
    0 and n+1 are sinks
    """ 
    g = graphToMultiDigraph(nx.path_graph(n+2))
    #remove arc 0->1 and n+1->n ?
    g.nodes[0]['sink'] = True
    g.nodes[n+1]['sink'] = True
    return g

def sbp_configuration(descr):
    """
    returns the configuration corresponding to the description
    in the len(descr) standard binary path 
    descr is a sequence of either 'L' and 'R' or -1/1 or 0/1
    """
    conf = {}
    for i in range(1, len(descr)):
        pass


