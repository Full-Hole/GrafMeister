from prettytable import PrettyTable

class GrafEdges:

    def __init__(self, nodesList, edgesList):
        self.edges = self.get_graf_edges(edgesList)
        self.nodes = nodesList

    def show(self):
        t = PrettyTable(['From','To', 'Weight'])
        for i in range(len(self.edges)):        
            t.add_row(self.edges[i])
        print(t) 

    def get_graf_edges(self, edgesList):
        edges = []
        for i in range(len(edgesList)):
            for j in range(len(edgesList[i])):
                if edgesList[i][j] !=0:
                    edges.append([i+1, j+1,edgesList[i][j]])
        return edges

    def get_id(self, nodeName):
        return self.nodes.index(nodeName)+1

    def get_neighbours(self, nodeName):
        node_id =self.get_id(nodeName)
        neighbours = self.get_neighbours_by_id(node_id)
        n_names=[]
        for i in neighbours:
            n_names.append(self.get_name_by_id(i))
        return n_names

    def get_name_by_id(self, i):
        return self.nodes[i-1]

    def get_neighbours_by_id(self, i):
        neighbours = []
        for row in self.edges:
            if row[0] == i:
                neighbours.append(row[1])
                continue
            if row[1] == i:
                neighbours.append(row[0])
        return neighbours

    def is_node_exist(self,name):
        if name in self.nodes:
            return True;
        return False;

    def is_id_exist(self, i):
        if i > 0 and i < len(self.nodes)+1:
            return True;
        return False;
