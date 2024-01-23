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

    def show(self):
        t = PrettyTable(['No','Name', 'C', 'P', 'List(C)', 'List(P)', 'weights of C', 'weights of P' ])
        t.title = 'C - Child, P - Parent'
        for i in range(len(self.graf)):        
            t.add_row(self.graf[i])                
        print(t)

    def get_names_by_ids(self, idList):
        nameList =[]
        for i in idList:
            nameList.append(self.graf[i-1][1])
        return nameList

    def get_neighbours(self, nodeName):
        for node in self.graf:
            if node[1] == nodeName:
                return self.get_names_by_ids(node[4]+node[5])
        return []

    def get_neighbours_by_id(self, i):
        if i > 0 and i < len(self.graf):
            return self.graf[i-1][4] + self.graf[i-1][5]
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

    def has_chain(self, idList):
        chainLength = len(idList)
        childs = []
        for i in range(chainLength):
            if i+1 < chainLength:
                childs = self.graf[idList[i]-1][4]
                if idList[i+1] not in childs:
                    return False
        return True  

    def has_chain_by_name(self, nodeList):
        idList = self.get_ids(nodeList, self.graf)
        return self.has_chain(idList, self.graf)


    def find_nodes_by_weight(self,weight):
        nodes =[]
        for row in self.graf:
            weights = sum(row[6]+row[7])
            if weights > weight:
                nodes.append(row[0])
        return nodes

    def calc_edges(self):
        edge = 0;
        for row in self.graf:
            edge += row[2];
        return edge;

    def is_id_exist(self,i):
        if i > 0 and i < len(self.graf)+1:
            return True;
        return False;

    def is_node_exist(self,name):
        for node in self.graf:
            if node[1] == name:
                return True;
        return False;

    