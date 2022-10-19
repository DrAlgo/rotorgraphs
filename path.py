from rotorgraphs import *

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
    descr is a list or str of either 'L' and 'R' or -1/1 or 0/1
    """
    rho = {}
    for i in range(1, len(descr)+1):
        rho[i] = 0 if descr[i-1] in ['L', '0', 0, -1] else 1
    return rho

def sbp_rotor_configuration_class_number(rho):
    """returns the index of the class of rotors of configuration rho,
    i.e. the number of 1

    Args:
        rho (dict(node:int)): rotor configuration

    Returns:
        int : class number
    """    
    return sum(rho.values())