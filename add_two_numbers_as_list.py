'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
'''
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def add(head1, head2):
	carry = 0 
	prev = None
	result_head = None

	while head1 and head2:
		new_node =  Node(((head1.val + head2.val + carry) % 10))
		if prev == None:
			result_head = new_node
		else:
			prev.next = new_node

		carry  = (head1.val + head2.val + carry) / 10
		prev = new_node
		head1 = head1.next
		head2 = head2.next

	while head2:
		new_node = Node(((head2.val + carry) % 10))

		prev.next = new_node
		carry  = (head2.val + carry) / 10
		prev = new_node
		head2 = head2.next

	while head1:
		new_node = Node(((head1.val + carry) % 10))
		prev.next = new_node
		carry  = (head1.val + carry) / 10
		prev = new_node
		head1 = head1.next

	if carry > 0:
		prev.next = Node(carry)

	return result_head



import scratch_pad
a = scratch_pad.a
b = scratch_pad.b
result = add(a,b)
scratch_pad.print_list(a)
print ''
scratch_pad.print_list(b)
print 
scratch_pad.print_list(result)