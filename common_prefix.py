from collections import deque

def commom_prefix(array):

	my_deque = deque(array)
	
	while len(my_deque) > 1:
		first_string = my_deque.popleft()
		second_string = my_deque.popleft()
		prefix = get_prefix(first_string, second_string)
		my_deque.appendleft(prefix)

	return my_deque[0]
	
def get_prefix(s1, s2):
	result = []
	i = 0 
	j = 0
	while i < len(s1) and j < len(s2):
		if s1[i] == s2[j]:
			result.append(s1[i])
			i+=1
			j+=1
		else:
			return ''.join(result)
	return ''.join(result)
array = [

  "abcdefgh",

  "aefghijk",

  "abcefgh"
]
print commom_prefix(array)

