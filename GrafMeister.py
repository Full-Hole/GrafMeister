import networkx as nx
import matplotlib.pyplot as plt
import timeit
from prettytable import PrettyTable
from getsize import get_size
from grafarray import GrafArray
from grafmatrix import GrafMatrix
from grafedges import GrafEdges

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

def is_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def main_menu():
    while True:
        show_main_menu()
        i = input("Ваш выбор: ")
        match i:
            case '1': g = GrafMatrix(V,E)
            case '2': g = GrafEdges(V,E)
            case '3': g = GrafArray(V,E)
            case '4': 
                g = parse_graph(V,E)
                show_graph(g)
                continue
            case '5': 
                size_menu()
                continue
            case '6': 
                test_menu()
                continue
            case '0': raise SystemExit
            case _ : 
                print('Некорректный ввод')
                continue
        side_menu(g)

def side_menu(g):
    while True:
        show_side_menu()
        i = input("Ваш выбор: ")
        match i:
            case '1': neighbours_menu(g)
            case '2': chain_menu(g)
            case '3': weight_menu(g)
            case '4': print("В заданном графе ", g.calc_edges(), " ребер")
            case '5': g.show()
            case '0': break
            case _ : continue        

def neighbours_menu(g):
    print("")
    node = input("Введите Id или Имя вершины: ")
    out = ''
    if is_int(node):
        if g.is_id_exist(int(node)):
            print("Соседи вершины ",node, ' - ', g.get_neighbours_by_id(int(node)))
            return    
    else:
        if g.is_node_exist(node):
            print("Соседи вершины ",node, ' - ',g.get_neighbours(node))
            return
    print('Вершина не найдена')

def chain_menu(g):
    print("")
    ids = []
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

def size_menu():
    print("")
    t = PrettyTable(['Объект', 'Размер в байтах'])
    t.title = 'Размер объектов'
    t.align['Объект'] = "l"
    t.add_row(['Матрица смежности', get_size(GrafMatrix(V,E).graf)])
    t.add_row(['Список ребер', get_size(GrafEdges(V,E).graf)])
    t.add_row(['Массив записей', get_size(GrafArray(V,E).graf)])
    print(t)

    input("Введите символ для возвращения в предыдущее меню")

def test_menu():
    setVar = {'Матрица смежности':"g = GrafMatrix(V,E)", 
              'Список ребер':"g = GrafEdges(V,E)",
              'Массив записей':"g = GrafArray(V,E)"}
    setFunc = {'получение соседей':"g.get_neighbours_by_id(5)",
              'проверка цепи':"g.has_chain([1,2,3,4,6,7,8,9])",
              'поиск вершин по стоимости':"g.find_nodes_by_weight(10)",
              'подсчет граней':"g.calc_edges()"}

    print("Подсчет времени выполнения подпрограм")
    for key, val in setVar.items():
        t = PrettyTable(['Название функции', 'Время выполнения 10^6 раз', 'средее время'])
        t.title = key
        t.align['Название функции'] = "l"
        for k, v in setFunc.items():
            time= get_counted_time(v,val)
            t.add_row([k, time,time/1000000])
        print(t)

    input("Введите символ для возвращения в предыдущее меню")

def get_counted_time(sm,st):
    return timeit.timeit(stmt=sm,setup=st,globals=globals())

def show_main_menu():
    t = PrettyTable(['№', 'Выбор'])
    t.title = "Представление графов в ЭВМ"
    t.align['Выбор'] = "l"
    t.add_row(['1','Матрица смежности'])
    t.add_row(['2','Список ребер'])
    t.add_row(['3','Массив записей'],divider=True)
    t.add_row(['4','Показать граф'])
    t.add_row(['5','Размер объектов'])
    t.add_row(['6','Время выполнения'],divider=True)
    t.add_row(['0','Выход'])
    print(t)

def show_side_menu():
    t = PrettyTable(['№', 'Выбор'])
    t.align['Выбор'] = "l"
    t.title = "Представление графов в ЭВМ"
    t.add_row(['1','Соседи заданной вершины'])
    t.add_row(['2','Создает ли последовательность цепь'])
    t.add_row(['3','Номера вершин, сумма весов ребер которых больше заданной величины'])
    t.add_row(['4','Количество ребер в графе'])
    t.add_row(['5','Отобразить'],divider=True)
    t.add_row(['0','Назад'])
    print(t)
 
main_menu()