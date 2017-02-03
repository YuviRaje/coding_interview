'''
Roman to Integer

hash_map = {'X':10,'I':1,'V':5,'L':50,'C':100,'D':500,'M':1000}
XI
'''


hash_map = {'X':10,'I':1,'V':5,'L':50,'C':100,'D':500,'M':1000}
sample_input = 'MXI'
def roman_to_integer(A, hash_map):
	i = 0
	result = 0
	while i < len(A):

		if i + 1 <= len(A) - 1 and hash_map[A[i+1]] > hash_map[A[i]]:
			result += hash_map[A[i+1]] - hash_map[A[i]]
			i+=2
		else:
			result += hash_map[A[i]]
			i+=1

	return result
print roman_to_integer(sample_input, hash_map)