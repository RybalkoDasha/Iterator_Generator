nested_list =  [
	['a', 1, 'c'],
	['d', 'e', 'f'],
	[1, 2, [], 'dsjdj', 98, {}],
]
flat_list = []

def FlatGenerator(nested_list):
	for el in nested_list:
		if type(el) == list:
			FlatGenerator(el)
		else:
			flat_list.append(el)
	return flat_list

if __name__ == '__main__':
	print(FlatGenerator(nested_list))