from prettytable import PrettyTable

class GrafArray:    

    def __init__(self, nodes, edges):
        self.graf = self.get_graf_array(nodes, edges)

    def get_child(self,row):
        childs ={}
        for i in range(len(row)):
            if row[i] !=0:
                childs[i+1]=row[i]
        return childs

    def get_parent(self, data, collnum):
        parents ={}
        for i in range(len(data)):
            if data[i][collnum] !=0:
                parents[i+1]=data[i][collnum]
        return parents   

    def get_graf_array(self, nodes, edges):
        graf=[]
        for i in range(len(edges)):
            ch = self.get_child(edges[i])
            pr = self.get_parent(edges, i)
            graf.append([i+1,nodes[i], len(ch), len(pr), 
                      list(ch.keys()), list(pr.keys()),
                      list(ch.values()), list(pr.values())])
        return graf

    def show_graph_table(self):
        t = PrettyTable(['No','Name', 'C', 'P', 'List(C)', 'List(P)', 'weights of C', 'weights of P' ])
        t.title = 'C - Child, P - Parent'
        for i in range(len(self.graf)):        
            t.add_row(self.graf[i])                
        print(t)

    def get_neighbours(self, nodeName):
        for node in self.graf:
            if node[1] == nodeName:
                return node[2]+node[3]
        return []

    def get_id(self, nodeName):
        for i in range(len(self.graf)):
                if(nodeName==self.graf[i][2]):
                    return i+1
    
    def get_ids(self, nodeList):
        idList =[]
        for j in range(len(nodeList)):
            idList.append(self.get_id(nodeList[j], self.graf))        
        return idList;

    def has_chain_by_ids(self, idList):
        chainLength = len(idList)
        childs = []
        for i in range(chainLength):
            if i+1 < chainLength:
                childs = self.graf[idList[i]-1][4]
                if idList[i+1] not in childs:
                    return False
        return True  

    def has_chain(self, nodeList):
        idList = self.get_ids(nodeList, self.graf)
        return self.has_chain_by_ids(idList, self.graf)


    def find_nodes_by_weight(self,weight):
        return 0

    def calc_edges(self):
        return 0
    