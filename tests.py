from path import *
from rotorgraphs import *
from itertools import product

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



def test_verif_groupe_chaine1(n):
        """
        pour toutes les configurations de depart sur n sommets non sink, on 
        route une particle et une antiparticule
        depuis chaque sommet, et on vérifie que les numeros de classes correspondent bien
        """
        g = standard_binary_path(n)

        #enumeration des configurations
        for descr in product(['0','1'], repeat = n):
                for v in range(1,n+1):
                        #particle
                        rho1 = sbp_configuration(descr)
                        n1 = sbp_rotor_configuration_class_number(rho1)
                        flow = rout_single_particle(g, rho1, v)
                        n2 = sbp_rotor_configuration_class_number(rho1)

                        #verification
                        assert n2 == (n1 + v) % (n+1)
                        print(f"{n1} + {v} == {n2} mod {n+1}", end = ", ")

                        #antiparticle
                        rho1 = sbp_configuration(descr)
                        n1 = sbp_rotor_configuration_class_number(rho1)
                        flow = rout_single_particle(g, rho1, v, -1)
                        n2 = sbp_rotor_configuration_class_number(rho1)

                        #verification
                        assert n2 == (n1 - v) % (n+1)
                        print(f"{n1} - {v} == {n2} mod {n+1}")

test_verif_groupe_chaine1(10)