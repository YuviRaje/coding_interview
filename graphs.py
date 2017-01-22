from collections import defaultdict, deque

class Graph:
	def __init__(self):
		self.nodes = defaultdict(list)

	def add_edge(self, from_node, to_node):
		self.nodes[from_node].append(to_node)


	def depth_first_search(self, source, visited = None):
		if visited == None:
			visited = set()
		print source,
		visited.add(source)

		for each_neighbour in self.nodes[source]:
			if each_neighbour not in visited:
				self.depth_first_search(each_neighbour, visited)


	def breadth_first_search(self, source):
		visited = set()

		queue = deque([source])

		while len(queue) > 0:
			popped_node = deque.pop()
			visited.add(nodes)
			print nodes

			for each_neighbour in self.nodes[popped_node]:
				if each_neighbour not in visited:
					queue.append_left(each_neighbour)
