
def str_str(haystack, needle):
	if haystack == '' or needle == '':
		return -1 

	for i in range(len(haystack)):
		if needle[0] == haystack[i]:
			if compare_strings(needle,haystack, i):
				return i

	return -1 


def compare_strings(s1, s2, index):
	if s1 == s2[index: index+len(s1)]:
		return True
	return False


print str_str('asdsayaskasdsad', 'ya')