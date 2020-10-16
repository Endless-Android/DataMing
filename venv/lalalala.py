test_data = [ [1], [1, 2], [3, 4] ] 

def backtrack(data, data_index, result=[], current_res=[], target_len=3):
	if len(current_res) == target_len:
		result.append(','.join(map(str, current_res)))
		return
	if data_index >= len(data):
		return

	for i in range(len(data[data_index])):
		current_res.append(data[data_index][i])
		backtrack(data, data_index + 1, result, current_res, target_len)
		current_res.pop()
	return result

print(backtrack(test_data, 0))