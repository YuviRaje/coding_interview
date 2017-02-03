def subset(user_list, current_list, index, output):
	if index < 0:
		if current_list != '':
			output.append(current_list)
		return 

	subset(user_list, current_list + str(user_list[index]), index - 1, output )
	subset(user_list, current_list, index - 1, output)
	return output

user_list = [1,2,3]

print map(int, subset(user_list, '', len(user_list) - 1, []))