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