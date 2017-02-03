
class Node:
	def __init__(self, key, value):
		self.value = value
		self.next = None
		self.prev = None 
		self.key = key



class LRU:
	def __init__(self, capacity = 10):
		self.capacity = capacity
		self.cache = {}
		self.front = None
		self.rear = None
		

	def set(self, key, value):
		new_node = Node(key, value)

		if len(self.cache) <  self.capacity:
			self._add_front(new_node)
			self.cache[key] = new_node 

		else:
			last_key = self.delete_last()
			del self.cache[last_key]
			self._add_front(new_node)
			self.cache[key] = new_node

	def get(self, key):
		if key in self.cache:

			self._move_to_front(key)
			return self.cache[key].value
		else:
			return -1 


	def _add_front(self, new_node):
		if self.front == None:
			self.front = new_node
			self.rear = new_node
		else:
			self.front.prev = new_node
			new_node.next = self.front 
			self.front= new_node

	def _move_to_front(self, key):
		current_node = self.cache[key]
		self._delete_node(current_node)
		self._add_front(current_node)

	def _delete_node(self, current_node):
		if self.front == current_node:
			self.front = None
		else:
			current_node.prev.next = current_node.next
			if current_node.next:
				current_node.next.prev = current_node.prev
	
	def delete_last(self):
		last_node_key = self.rear.key
		self.rear.prev.next = None
		self.rear = self.rear.prev
		return last_node_key

my_lru = LRU(capacity = 3)
my_lru.set(1,'a')
my_lru.set(2,'b')
my_lru.set(3,'c')
my_lru.set(4,'d')
my_lru.set(5,'e')
my_lru.set(6,'f')









