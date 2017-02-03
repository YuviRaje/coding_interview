'''
Topological Sort
'''

from collections import deque
from collections import defaultdict

def topo_sort(adj_list, nodes):
	visited = set()
	stack = deque()
	for each_node in range(nodes):
		if each_node not in visited:
			dfs_search(each_node, visited, stack, adj_list)

	return list(stack) 


def dfs_search(current_node,visited, stack, adj_list):
	visited.add(current_node)

	for each_neighbour in adj_list[current_node]:
		if each_neighbour not in visited:
			dfs_search(each_neighbour, visited, stack, adj_list)

	stack.appendleft(current_node)




class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) 
        self.V = vertices 
 
    def addEdge(self,u,v):
        self.graph[u].append(v)


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);


print topo_sort(g.graph, g.V)