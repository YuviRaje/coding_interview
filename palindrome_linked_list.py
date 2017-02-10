

	def get_middle(head):
		slow = head 
		fast = head
		slow_prev = None

		while fast != None and fast.next != None:
			prev = slow
			slow = slow.next
			fast = fast.next.next

		return slow,prev


	def reverse(current_node):
		prev = None

		while current_node:
			next_node = current_node.next
			current_node.next = prev
			prev = current_node
			current_node = next_node

		return prev 


	def is_list_palin(head):

		middle_node, middle_prev = get_middle(head)

		new_middle_node = reverse(middle_node)
		middle_prev.next = None 

		A = head
		B = new_middle_node

		while A and B:
			if A.val != B.val:
				return False
			A = A.next
			B = B.next 

		return True


	import scratch_pad

	print is_list_palin(scratch_pad.a)