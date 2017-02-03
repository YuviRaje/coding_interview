from collections import defaultdict, deque


class Graph:
	def __init__(self):
		self.adj_list = defaultdict(list)

	def add_node(self, from_node, to_node):
		self.adj_list[from_node].append(to_node)

	def depth_first_search(self, source, visited = set()):

		print source, '->', 
		visited.add(source)
		for each_node in self.adj_list[source]:
			if each_node not in visited:
				self.depth_first_search(each_node)


my_graph = Graph()
my_graph.add_node(1,2)
my_graph.add_node(1, 3)
my_graph.add_node(4,9)
my_graph.add_node(2,3)
print my_graph.depth_first_search(1)