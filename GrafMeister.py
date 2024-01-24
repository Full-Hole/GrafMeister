import networkx as nx
import matplotlib.pyplot as plt
import menu as mm
from grafarray import GrafArray
from grafmatrix import GrafMatrix
from grafedges import GrafEdges
from prettytable import PrettyTable

print("Hello")
V = ['Pete', 'Stuart', 'George', 'John', 'Ringo', 'Paul', 'Tommy', 'Norman', 'Chas']
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


def main_menu():
    while True:
        mm.show_main_menu()
        i = input("Ваш выбор: ")
        match i:
            case '1': g = GrafMatrix(V,E)
            case '2': g = GrafEdges(V,E)
            case '3': g = GrafArray(V,E)
            case '0': raise SystemExit
            case _ : 
                print('Некорректный ввод')
                continue
        side_menu(g)



def side_menu(g):
    while True:
        mm.show_side_menu()
        i = input("Ваш выбор: ")
        match i:
            case '1': neighbours_menu(g);
            case '2': chain_menu(g);
            case '3': weight_menu(g);
            case '4': print("В заданном графе ", g.calc_edges(), " ребер");
            case '5': g.show()
            case '0': break;
            case _ : continue;
        

def neighbours_menu(g):
    print("")
    node = input("Введите Id или Имя вершины: ");
    out = '';
    if is_int(node):
        if g.is_id_exist(int(node)):
            print("Соседи вершины ",node, ' - ', g.get_neighbours_by_id(int(node)));
            return    
    else:
        if g.is_node_exist(node):
            print("Соседи вершины ",node, ' - ',g.get_neighbours(node));
            return
    print('Вершина не найдена');

def chain_menu(g):
    print("")
    ids = [];
    ans =''
    t = input("Введите цепочку вершин через пробел: ")
    ids = t.split()
    for i in range(len(ids)):
        if not is_int(ids[i]):
            print("Введены некоретные данные")
            return
    if g.has_chain(list(map(int, ids))):
        ans='сущесвует'
    else:
        ans='отсутствует'

    print("Цепочка ", ids, " - ", ans )

def weight_menu(g):
    print("")
    w = input("Задайте величину: ")
    if is_int(w):
        print("Список вершин ", g.find_nodes_by_weight(int(w)))
    else:
        print("Введены некоретные данные")


def is_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False




    

#gred = ge.get_graf_edges(V,E)
#ge.print_edges(gred)
#Получение цепочки из ввода
#chain = input_chain()
main_menu()




#grafArray.show_graph_table()


G = parse_graph(V,E)
show_graph(G)
#i = input()



