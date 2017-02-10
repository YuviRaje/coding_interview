class Node:
	def __init__(self,data):
		self.val = data
		self.next = None

a = Node(9)
a.next = Node(9)
a.next.next = Node(9)



b = Node(1)



def print_list(current_node):
	while  current_node:
		print current_node.val, '->',
		current_node = current_node.next

	
