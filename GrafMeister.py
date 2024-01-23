import networkx as nx
import matplotlib.pyplot as plt
import grafedges as ge
from grafarray import GrafArray
import grafmatrix as gm
from prettytable import PrettyTable

print("Hello")
V = ('Pete', 'Stuart', 'George', 'John', 'Ringo', 'Paul', 'Tommy', 'Norman', 'Chas')
E = [
[0, 6, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 3, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 4, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 1, 4, 0, 0],
[0, 0, 3, 1, 0, 0, 0, 0, 0],
[0, 0, 6, 0, 0, 0, 3, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 2, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 4],
[0, 0, 0, 0, 2, 0, 0, 0, 0],
]

def parse_graph(nodes, edges):
    G = nx.DiGraph()
    for v in nodes:
        G.add_node(v)
    for i in range(len(edges)):
        for j in range(len(edges[i])):
            if edges[i][j] !=0:
                G.add_edge(nodes[i], nodes[j], weight=edges[i][j])
    return G

def show_graph(G, custom_node_positions=None):
    plt.figure() 
    
    if custom_node_positions==None:
        pos = nx.circular_layout()
    else:
        pos=custom_node_positions
        
    weight_labels = nx.get_edge_attributes(G,'weight')
    nx.draw(G,pos,font_size =9, node_color = '#85ceff', node_size = 1000, with_labels = True,)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=weight_labels)
    plt.show()

def input_chain():
    x=True
    ids = [] 
    while(x):
        print("Введите цепочку вершин через пробел:")
        t = input()
        if isinstance(t, str):
            ids = t.split()
            for i in range(len(ids)):
                if isinstance(ids[i], int):
                    print("Введены некоретные данные")
                    break
            x=False
            print("Введены слудцющие значения ", ids)
            return list(map(int, ids))



#gred = ge.get_graf_edges(V,E)
#ge.print_edges(gred)



grafArray = GrafArray(V,E)

par = input_chain()

grafArray.show_graph_table()

#print(grafArray.has_chain_by_ids(par))
#G = parse_graph(V,E)
#show_graph(G)
#i = input()



