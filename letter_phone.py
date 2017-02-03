'''
Given a digit string, return all possible letter combinations that the number could represent.
'''

keyboard_map = {
	2: ['a', 'b','c'],
	3: ['d', 'e', 'f']
}

def get_all_words(keyboard_map, input_keys = [2,3]):
	return _get_all_words(keyboard_map, input_keys, 0, '', [])

def _get_all_words(keyboard_map, input_keys, current_key_index, current_word, result):

	if current_key_index == len(input_keys):
		result.append(current_word)
		return 

	for each_alphabet in keyboard_map[input_keys[current_key_index]]:
		_get_all_words(keyboard_map, input_keys, current_key_index + 1, current_word + each_alphabet, result)

	return result


print get_all_words(keyboard_map)