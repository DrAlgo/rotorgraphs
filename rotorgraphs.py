import networkx as nx
import copy


#useful functions
identity = lambda x:x

def graphToMultiDigraph(g):
    """
    takes an undirected graph and returns a multi directed graph
    with two arcs for each previous edge

    Args:
        g (nx.Graph): standard undirected graph

    Returns:
        nx.MultiDigraph: corresponding multi digraph
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

def turn(g, v, rho, k=1):
    """turns configuration rho at vertex v in graph g by quantity k

    Args:
        g (nx.MultiDigraph): base rotorgraph
        v (hashable): vertex
        rho (dict(node:int)): rotor configuration
        k (int, optional): _description_. Defaults to 1.
    """
    rho[v] = (rho[v] + k ) % g.out_degree(v)

def move(sigma, arc, k=1) -> None:
    """moves k chips along given arc  in g in chips config sigma

    Args:
        sigma (dict(node:int)):chips config
        a (tuple(node,node,int)): arc
        k (int, optional): quantity moved. Defaults to 1.
    """
    sigma[arc[0]] -= k
    sigma[arc[1]] += k
    
def single_rotor_step(g, sigma, rho, v, direction):
    """_summary_

    Args:
        g (_type_): _description_
        sigma (_type_): _description_
        rho (_type_): _description_
        v (_type_): _description_
        direction (int): +1 for a particle or -1 for an antiparticle

    Returns:
        hashable : new position of the routed particle / antiparticle
    """  

    if direction == +1:
        a = list(g.edges(v))[rho[v]]
        move(sigma, a)
        turn(g, v, rho, 1)
        
    elif direction == -1:
        turn(g, v, rho, -1)
        a = list(g.edges(v))[rho[v]]
        move(sigma, a)
    return a[1]

def rout_single_particle(g, rho, v_start, direction = +1):
    
    sigma = {w:0 for w in g.nodes} #not really used here
    sigma[v_start] = 1

    v_current = v_start
    while g.nodes[v_current]['sink'] == False:
        v_current = single_rotor_step(g, sigma, rho, v_current, direction)


def standard_rotor_config(g, with_sinks=False):
    """returns a rotor configuration
    with the first stored arc for every vertex"""
    return {v : 0 for v in g.nodes if g.degree(v) > 0 and g.nodes[v]['sink']==with_sinks}

def non_sink_nodes(g):
    return (v for v in g.nodes(data=True) if g.nodes[v]['sink']==False)





