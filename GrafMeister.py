import networkx as nx
import matplotlib.pyplot as plt
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

def get_child(row):
    childs ={}
    for i in range(len(row)):
        if row[i] !=0:
            childs[i+1]=row[i]
    return childs

def get_parent(data, collnum):
    parents ={}
    for i in range(len(data)):
        if data[i][collnum] !=0:
            parents[i+1]=data[i][collnum]
    return parents


def show_graph_table(grafArray):
    t = PrettyTable(['No','Name', 'C', 'P', 'List(C)', 'List(P)', 'weights of C', 'weights of P' ])
    t.title = 'C - Child, P - Parent'
    for i in range(len(grafArray)):        
        t.add_row(grafArray[i])                
    print(t)

def get_graf_array(nodes, edges):
    graf=[]
    for i in range(len(edges)):
        ch = get_child(edges[i])
        pr = get_parent(edges, i)
        graf.append([i+1,nodes[i], len(ch), len(pr), 
                  list(ch.keys()), list(pr.keys()),
                  list(ch.values()), list(pr.values())])
    return graf


def print_edges(grafEdges):
    t = PrettyTable(['From','To', 'Weight'])
    for i in range(len(grafEdges)):        
        t.add_row(grafEdges[i])
    print(t) 

def get_graf_edges(nodes, edges):
    graf = []
    for i in range(len(edges)):
        for j in range(len(edges[i])):
            if edges[i][j] !=0:
                graf.append([nodes[i], nodes[j],edges[i][j]])
    return graf



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
    
gred = get_graf_edges(V,E)
print_edges(gred)
grar = get_graf_array(V,E)
show_graph_table(grar)
#G = parse_graph(V,E)
#show_graph(G)
#i = input()



