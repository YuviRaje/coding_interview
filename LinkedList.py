
'''
API's include 
1. append() -> O(n)
2. append_left() -> O(1)
3. pop() -> O(n)
4. pop_left() -> O(1)
5. print_list() -> O(n)
Space -> O(n)

'''

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
			while current_node.next != None:
				current_node = current_node.next
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
		if self.head == None :
			raise Exception('Cannt remove from empty list')

		current_node = self.head 
		prev = None
		while current_node.next != None:
			prev = current_node
			current_node = current_node.next
		
		if prev == None:
			self.head = None
		else:
			prev.next = None 

	def pop_left(self):
		current_node = self.head
		if current_node == None:
			raise Exception('Cant remove from emtry list')

		self.head = self.head.next

	def print_list(self):

		current_node = self.head
		while current_node:
			print current_node.data, '- >',
			current_node = current_node.next 

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append_left(0)
linked_list.pop_left()

linked_list.pop_left()
linked_list.print_list()































