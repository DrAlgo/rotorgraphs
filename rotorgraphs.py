import networkx as nx
import copy


#type Aliases
RotorGraph = nx.MultiDiGraph
RotorConfig = {int:int}
Vertex = int | str

#useful functions
identity = lambda x:x

def graphToMultiDigraph(g:nx.Graph) -> nx.MultiDiGraph:
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
A rotor configuration is a dict {node:index}
the rotor order on a node a is the order in the dict g[a]

each node should contain a property "sink" set to True of False
"""

def turn(g:RotorGraph, v:Vertex, rho:RotorConfig, k=1) -> None:
    """
    turns configuration rho at vertex x in graph g by quantity k
    """
    rho[v] = (rho[v] + k ) % g.degree(v)

def move(g:RotorGraph, v:Vertex, rho:RotorConfig, k=1) -> None:
    """
    moves k chips along arc rho[v]
    """


def standard_rotor_config(g, with_sinks=False):
    """returns a rotor configuration
    with the first stored arc for every vertex"""
    return {v : 0 for v in g.nodes if g.degree(v) > 0 and g.nodes[v]['sink']==with_sinks}

def non_sink_nodes(g):
    return (v for v in g.nodes(data=True) if g.nodes[v]['sink']==False)

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



