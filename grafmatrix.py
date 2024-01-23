from prettytable import PrettyTable

class GrafMatrix:

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.graf = (nodes,edges)

    def show(self):
        t=PrettyTable(['Name']+self.graf[0])
        for i in range(len(self.graf[0])):
            t.add_row([self.graf[0][i]]+self.graf[1][i], divider=True)
        print(t)

    def is_id_exist(self, i):
        if i > 0 and i < len(self.graf[0])+1:
            return True;
        return False;

    def get_neighbours(nodeName, grafMatrix):
        return 'fuckoff'

    def get_neighbours_by_id(self, i):
        row = self.edges[i-1];
        size = len(row)
        neighbours =[]
        for j in range(size):
            if row[j] !=0:
                neighbours.append(j+1)
        for r in range(size):
            if self.edges[r][i-1] !=0:
                neighbours.append(r+1)
        return neighbours

    def calc_edges(self):
        return 'fuckoff'
