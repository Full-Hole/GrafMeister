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

def get_neighbours(nodeName, grafEdges):
    print ('fuckoff')