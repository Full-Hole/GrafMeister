from prettytable import PrettyTable

class GrafEdges:

    def __init__(self, nodes, edges):
        self.graf = self.get_graf_edges(nodes,edges)

    def show(self):
        t = PrettyTable(['From','To', 'Weight'])
        for i in range(len(self.graf)):        
            t.add_row(self.graf[i])
        print(t) 

    def get_graf_edges(self, nodes, edges):
        graf = []
        for i in range(len(edges)):
            for j in range(len(edges[i])):
                if edges[i][j] !=0:
                    graf.append([nodes[i], nodes[j],edges[i][j]])
        return graf

    def get_neighbours(self, nodeName):
        return 'fuckoff'