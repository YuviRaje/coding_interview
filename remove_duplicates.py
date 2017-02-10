'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''


def remove_dups(head):
	my_set = set()
	prev = None
	while head:
		if head.val not in my_set:
			if prev != None:
				prev.next = head
			my_set.add(head.val)
			prev = head
		head = head.next
	prev.next = None



def remove_dups_without_space(head):
	prev = None 

	current_node = head
	while current_node:
		if prev != None:
			while current_node != None and prev.val == current_node.val:
				current_node = current_node.next

		if prev:
			prev.next = current_node
		if current_node:
			prev = current_node
			current_node = current_node.next



import scratch_pad

a = scratch_pad.a 
remove_dups_without_space(a)
scratch_pad.print_list(a)

