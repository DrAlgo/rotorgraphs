# rotorgraphs

Utilise la bibliothèque NetworkX
* La classe utilisée pour les rotor graphs est la classe MultiDigraph
* Les arcs sont naturellement ordonnés dans un MultiDigraph pour chaque sommet
    ```py
    g = nx.MultiDiGraph([[1,2],[1,2],[1,3],[2,3]])
    print(list(g.out_edges(1)))
    ```
    donne un itérateur sur 
    ```py
    [(1, 2), (1, 2), (1, 3)]
    ```
  

