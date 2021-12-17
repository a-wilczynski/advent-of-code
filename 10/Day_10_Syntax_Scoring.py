with open('input.txt') as f:
	input_ = [x.strip() for x in f.readlines()]

	score_table = {
	')' : 3,
	']': 57,
	'}': 1197,
	'>': 25137
	}

	pairs = {
	')': '(',
	']': '[',
	'}': '{',
	'>': '<' 
	}

	score = []
	for line in input_:
		chunk_opener = []
		chunk_closer = []
		flag = True

		for c in line:
			if c in '<[{(':
				chunk_opener.append(c)
			elif pairs[c] == chunk_opener.pop():
				continue
			else:
				score.append(score_table[c])
				break

	print(sum(score))





