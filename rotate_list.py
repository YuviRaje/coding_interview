'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''


def rotate(head, key):

	current_node = head
	prev = None
	for _ in range(k):
		prev = current_node
		current_node = current_node.next 

	prev.next = None

	while current_node.next:
		current_node = current_node.next

	current_node.next = head 
	

