import networkx as nx
import matplotlib.pyplot as plt
import grafedges as ge
import grafarray as ga
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
        pos = nx.circular_layout(G)
    else:
        pos=custom_node_positions
        
    weight_labels = nx.get_edge_attributes(G,'weight')
    nx.draw(G,pos,font_size =9, node_color = '#85ceff', node_size = 1000, with_labels = True,)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=weight_labels)
    plt.show()
    
gred = ge.get_graf_edges(V,E)
ge.print_edges(gred)
grar = ga.get_graf_array(V,E)
ga.show_graph_table(grar)
#G = parse_graph(V,E)
#show_graph(G)
#i = input()



