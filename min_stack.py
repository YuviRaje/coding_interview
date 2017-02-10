
'''
Min Stack. 
All operations are performed in O(1) time.
'''


class MinStack:
	def __init__(self):
		self.stack = []
		self.min_stack = []

	def push(self, value):
		if len(self.min_stack) == 0 or value < self.min_stack[-1]:
			self.min_stack.append(value)

		self.stack.append(value)

	def pop(self):
		if len(self.stack):
			popped_node = self.stack.pop()
			if popped_node == self.min_stack[-1]:
				self.min_stack.pop()
		else:
			raise Exception('cant pop from empty stack')

	def get_min(self):
		if len(self.min_stack):
			return self.min_stack[-1]
		else:
			raise Exception('stack is emmpty')

my_stack = MinStack()
my_stack.push(1)
my_stack.push(2)

print my_stack.get_min()
