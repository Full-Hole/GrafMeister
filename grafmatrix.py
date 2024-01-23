from prettytable import PrettyTable

class GrafMatrix:

    def __init__(self, nodes, edges):
        self.graf = (nodes,edges)

    def show(self):
        t=PrettyTable(['Name']+self.graf[0])
        for i in range(len(self.graf[0])):
            t.add_row([self.graf[0][i]]+self.graf[1][i], divider=True)
        print(t)

    def get_neighbours(nodeName, grafMatrix):
        return 'fuckoff'

    def get_neighbours_by_id(self, i):
        return 'fuckoff'

    def calc_edges(self):
        return 'fuckoff'
