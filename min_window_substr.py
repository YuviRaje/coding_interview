
'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".
'''


def min_window_substr(S,T):
	substr_char_map = fill_char_map(T)

	char_map = [0]*26
	i = 0
	j = 0
	max_window_length = float('inf')

	for each_char in S:

		char_map[ord(each_char) - ord('A')] += 1

		if covers_all_chars(char_map, substr_char_map):
			while covers_all_chars(char_map, substr_char_map):
				char_map[ord(S[i]) - ord('A')] -= 1
				i += 1

			i -= 1
			char_map[ord(S[i]) - ord('A')] += 1
			max_window_length = min(max_window_length, (j-i+1))

		j += 1

	return max_window_length

def fill_char_map(T):
	char_map = [0] * 26
	for each_char in T:
		char_map[ord(each_char) - ord('A')] += 1
	return char_map

def covers_all_chars(map1, map2):
	for i in range(26):
		if map2[i] >0 and map2[i] > map1[i]:
			return False
	return True

S = "ADOBECODEBANC"
T = "ABC"

print min_window_substr(S,T)


