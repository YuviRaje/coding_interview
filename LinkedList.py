
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None 


	def append(self, value):
		new_node = Node(value)
		current_node = self.head 
		if current_node == None:
			self.head = new_node
		
		else:
			while current_node.next:
				current_node = current_node
			current_node.next = new_node

	def append_left(self, value):
		new_node = Node(value)
		current_node = self.head 
		if current_node == None:
			self.head = new_node
		else:

			new_node.next = self.head 
			self.head = new_node


	def pop(self):

		current_node = self.head 
		prev = None
		while current_node.next != None:
			prev = current_node
			current_node = current_node.next
		if self.head == None :
			raise Exception('Cannt remove from empty string')
		elif prev == None:
			self.head = None
		else:
			prev.next = None 
			
	def reverse(self):
		prev = None 
		current_node = self.head

		while current_node:
			next_node = current_node.next
			current_node.next = prev 
			prev = current_node
			current_node = next_node
		self.head = prev

	def print_list(self):
		current_node = self.head
		while current_node:
			print current_node.data, '->', 
			current_node = current_node.next

a = LinkedList()

a.reverse()
a.print_list()

