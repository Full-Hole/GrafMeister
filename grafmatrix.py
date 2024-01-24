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
            return True
        return False

    def get_id(self, nodeName):
        return self.nodes.index(nodeName)+1

    def get_ids(self, nodeList):
        idList =[]
        for j in range(len(nodeList)):
            idList.append(self.get_id(nodeList[j]))        
        return idList

    def get_name_by_id(self, i):
        return self.nodes[i-1]

    def get_neighbours(self, nodeName):
        node_id =self.get_id(nodeName)
        neighbours = self.get_neighbours_by_id(node_id)
        n_names=[]
        for i in neighbours:
            n_names.append(self.get_name_by_id(i))
        return n_names

    def get_neighbours_by_id(self, i):
        return self.get_childs(i)+ self.get_parents(i)

    def is_node_exist(self,name):
        if name in self.nodes:
            return True
        return False

    def get_parents(self, i):
        col = self.column(i-1)
        parent=[]
        for j in range(len(self.edges)):
            if col[j] !=0:
                parent.append(j+1)
        return parent

    def get_childs(self, i):
        row = self.edges[i-1]
        children=[]
        for j in range(len(self.edges)):
            if row[j] !=0:
                children.append(j+1)
        return children
            
    def has_chain(self, idList):
        chainLength = len(idList)
        childs = []
        for i in range(chainLength):
            if i+1 < chainLength:
                childs = self.get_childs(idList[i])
                if idList[i+1] not in childs:
                    return False
        return True  

    def has_chain_by_name(self, nodeList):
        try:
            idList = self.get_ids(nodeList)
            return self.has_chain(idList)
        except ValueError:
            return False

    def get_parents_weight(self, i):        
        return self.column(i)

    def get_childs_weight(self, i):     
        return self.edges[i]

    def column(self, i):
        return [row[i] for row in self.edges]

    def find_nodes_by_weight(self,weight):
        nodesList =[]
        for i in range(len(self.nodes)):
            weights = sum(self.get_childs_weight(i)+self.get_parents_weight(i))
            if weights > weight:
                nodesList.append(i+1)
        return nodesList

    def calc_edges(self):
        sumEdges=0
        for i in range(len(self.edges)):
            sumEdges+=self.count_not_zero(self.edges[i])
        return sumEdges

    def count_not_zero(self, numList):
        j=0
        for i in numList:
            if i!=0:
                j+=1
        return j

