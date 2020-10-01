import math
from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt
pr = 0
NODE= 1
PATH = 2

class Graph:
    def __init__(self, Root=None):
        self.vertices = set(Root)
        self.edges = {}
        if (Root is not None):
            self.edges[Root] = list()

    def addnode(self, vertex):
        if (vertex in self.vertices):
            print('This vertex is already in graph')
        else:
            self.vertices.add(vertex)
            self.edges[vertex] = list()

    def addedge(self, vertex1, vertex2, edge_cost):
        if (vertex1 in self.vertices):
            self.edges[vertex1].append((edge_cost,vertex2 ))
        else:
            print('This vertex is not in graph. Add vertex first')

    def Markvisited(self):
        self.visitof = dict.fromkeys(self.vertices, False)

    def __str__(self):
        return str(self.edges)

    def UniformCostSearch_implement(self, root, goal):
        priortyq = PriorityQueue()
        priortyq.put((0, root, root))
        while (not (priortyq.empty())):
            node = priortyq.get()
            if (node[NODE] in goal):
                print(node[PATH])
                print(str(round(node[pr],1)))
                break
            elif(self.visitof[node[NODE]]==True):
                continue
            else:
                self.visitof[node] = True
                children = self.edges[node[NODE]]
                for child in children:
                    if (self.visitof[child[NODE]] is not True):
                        priortyq.put((child[pr] + node[pr], child[NODE], node[PATH] + "===>" + str(child[NODE]))) 
                    else:
                        continue

res=input("Enter the start node : ")
nes=input("Enter the end node : ")
G = nx.Graph()
G.add_node("Pernem",H = 4,pos = (3,11))
G.add_node("Panaji",H = 8.5,pos = (2,9))
G.add_node("Mapusa",H = 7,pos = (2,10))
G.add_node("Bicholim",H = 7.25,pos = (4,10))
G.add_node("Ponda",H = 5,pos = (3,8))
G.add_node("Dharbandora",H = 4.75,pos = (4,8))
G.add_node("Valpoi",H = 2.85,pos = (5,9))
G.add_node("Sanguem",H = 9.75,pos = (4,6))
G.add_node("Quepem",H = 3.65,pos = (3,4))
G.add_node("Margao",H = 5.95,pos = (1,5))
G.add_node("Marmugao",H = 2.2,pos = (1,6))
G.add_node("Chaudi",H = 1,pos = (3,3))
G.add_node("Canacona",H = 2.3,pos = (3,2))	
G.add_node("Vasco-da-gama",H = 1.25,pos = (1,7))
G.add_edge("Pernem", "Mapusa", weight=17.2 )
G.add_edge("Pernem", "Bicholim", weight=28)
G.add_edge("Mapusa", "Bicholim", weight=20.3)
G.add_edge("Mapusa", "Panaji", weight=16)
G.add_edge("Bicholim", "Ponda", weight=32.6)
G.add_edge("Bicholim", "Dharbandora", weight=33.7)
G.add_edge("Bicholim", "Valpoi", weight=21.7)
G.add_edge("Panaji", "Ponda", weight=31.4)
G.add_edge("Dharbandora", "Sanguem", weight=26.4)
G.add_edge("Valpoi", "Dharbandora", weight=27.8)
G.add_edge("Vasco-da-gama", "Marmugao", weight=2)
G.add_edge("Marmugao", "Margao", weight=30.6)
G.add_edge("Ponda", "Margao", weight=17.6)
G.add_edge("Ponda", "Quepem", weight=30)
G.add_edge("Ponda", "Sanguem", weight=32.4)
G.add_edge("Margao", "Quepem", weight=14.1)
G.add_edge("Sanguem", "Quepem", weight=13.2)
G.add_edge("Sanguem", "Canacona", weight=43.2)
G.add_edge("Quepem", "Chaudi", weight=33.7)
G.add_edge("Chaudi", "Canacona", weight=2.8)
pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos,with_labels = True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
print('# of edges: {}'.format(G.number_of_edges()))
print('# of nodes: {}'.format(G.number_of_nodes()))

g = Graph(res)
g.addnode("Pernem")
g.addnode("Mapusa")
g.addnode("Bicholim")
g.addnode("Panaji")
g.addnode("Valpoi")
g.addnode("Vasco-da-gama")
g.addnode("Ponda")
g.addnode("Dharbandora")
g.addnode("Marmugao")
g.addnode("Sanguem")
g.addnode("Margao")
g.addnode("Quepem")
g.addnode("Chaudi")
g.addnode("Canacona")
#adding edges
g.addedge("Pernem", "Mapusa",17.2)
g.addedge("Pernem", "Bicholim",28)
g.addedge("Mapusa", "Bicholim",20.3)
g.addedge("Mapusa", "Panaji",16)
g.addedge("Bicholim", "Ponda",32.6)
g.addedge("Bicholim", "Dharbandora",33.7)
g.addedge("Bicholim", "Valpoi",21.7)
g.addedge("Panaji", "Ponda",31.4)
g.addedge("Dharbandora", "Sanguem",26.4)
g.addedge("Valpoi", "Dharbandora",27.8)
g.addedge("Vasco-da-gama", "Marmugao",2)
g.addedge("Marmugao", "Margao",30.6)
g.addedge("Ponda", "Margao", 17.6)
g.addedge("Ponda", "Quepem", 30)
g.addedge("Ponda", "Sanguem",32.4)
g.addedge("Margao", "Quepem", 14.1)
g.addedge("Sanguem", "Quepem",13.2)
g.addedge("Sanguem", "Canacona",43.2)
g.addedge("Quepem", "Chaudi", 33.7)
g.addedge("Chaudi", "Canacona",2.8)
g.addedge("Mapusa", "Pernem",17.2)
g.addedge("Bicholim", "Pernem",28)
g.addedge("Bicholim", "Mapusa",20.3)
g.addedge("Panaji", "Bicholim",16)
g.addedge("Ponda", "Bicholim",32.6)
g.addedge("Dharbandora", "Bicholim",33.7)
g.addedge("Valpoi", "Bicholim",21.7)
g.addedge("Ponda", "Panaji",31.4)
g.addedge("Sanguem", "Dharbandora",26.4)
g.addedge("Dharbandora", "Valpoi",27.8)
g.addedge("Marmugao", "Vasco-da-gama",2)
g.addedge("Margao", "Marmugao",30.6)
g.addedge("Margao", "Ponda", 17.6)
g.addedge("Quepem", "Ponda", 30)
g.addedge("Sanguem", "Ponda",32.4)
g.addedge("Quepem", "Margao", 14.1)
g.addedge("Quepem", "Sanguem",13.2)
g.addedge("Canacona", "Sanguem",43.2)
g.addedge("Chaudi", "Quepem", 33.7)
g.addedge("Canacona", "Chaudi",2.8)
g.Markvisited()
g.UniformCostSearch_implement(res,nes)
plt.savefig("Sumana_graphrep.png")
plt.show()