
'''
My Trie
'''


class Trie:
	def __init__(self):
		self.root = Node()

	def add_word(self, word):
		current_node = self.root 

		for each_char in word:
			if current_node.has_char(each_char) == False:
				current_node.create_link(each_char)
			current_node = current_node.get_link(each_char)

		current_node.is_end = True	

	def search_word(self, word):
		current_node = self.root 
		for each_char in word:
			if current_node.has_char(each_char) == False:
				return False
			current_node = current_node.get_link(each_char)
		if current_node.is_end == True:
			return True

		return False

	def search_prefix(self, prefix):
		current_node = self.root
		for each_char in prefix:
			current_node = current_node.get_link(each_char)
		output = []
		self._dfs_search(prefix, current_node, '', output)
		return output

	def _dfs_search(self, prefix, current_node, current_word, output):
		if current_node.is_end:
			output.append(prefix + current_word )
		if current_node == None:
			return 

		for i, each_link in enumerate(current_node.links):
			if each_link != None:
				self._dfs_search(prefix, each_link , current_word + chr(ord('a') + i), output)





my_trie = Trie()
my_trie.add_word('yask')
my_trie.add_word('yak')
my_trie.add_word('alan')

print my_trie.search_prefix('ya')