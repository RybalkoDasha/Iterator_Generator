def FlatGenerator(data):
		for elem in data:
			for el in elem:
				yield el


if __name__ == '__main__':
	nested_list = [
		['a', 'b', 'c'],
		['d', 'e', 'f'],
		[1, 2, None, 'Hi', 909],
	]

	flat_list = [item for item in FlatGenerator(nested_list)]
	print(flat_list)


