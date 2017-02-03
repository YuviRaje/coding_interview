'''
Tree depth
'''

def height(root):
	if root == None:
		return 0 

	left_subtree_height = height(root.left)
	right_subtree_height = height(root.right)

	return max(left_subtree_height, right_subtree_height) + 1


