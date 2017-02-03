'''
API's

pop() -> O(1)
pop_left() -> O(1)

append() -> O(1)
append_left() -> O(1)

print_list - > O(n)
'''

class Node:
	def __init__(self, value):
		self.value  = value
		self.next = None 
		self.prev = None 




class Dequeue:
	def __init__(self):
		self.front = None 
		self.rear = None 

	def append(self, value):
		new_node = Node(value)
		if self.rear == None:
			self.append_first(new_node)
		else:
			new_node.prev = self.rear
			self.rear.next = new_node
			self.rear = new_node

	def append_first(self, new_node):
		self.rear = new_node
		self.front = new_node

	def append_left(self, value):
		new_node = Node(value)
		if self.front == None:
			self.append_first(new_node)
		else:
			self.front.prev = new_node
			new_node.next = self.front
			self.front = new_node

	def pop(self):
		if self.rear == None:
			raise Exception('cant remove from empty list')
		if self.rear == self.front:
			self.rear = None 
			self.front = None 
		else:
			self.rear.prev.next = None
			self.rear = self.rear.prev

	def pop_left(self):
		if self.front == None:
			raise Exception('cant remove from empty list')

		if self.front == self.rear:
			self.front = None 
			self.rear = None 

		else:
			self.front = self.front.next

	def print_list(self):
		current_node = self.front 

		while current_node:
			print current_node.value, '- >', 
			current_node = current_node.next 


my_list = Dequeue()
my_list.append(1)
my_list.append(10)
my_list.pop()
my_list.pop_left()
my_list.append(2)
my_list.append_left(3)
my_list.pop()
my_list.print_list()