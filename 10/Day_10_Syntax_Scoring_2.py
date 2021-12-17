with open('input.txt') as f:
	input_ = [x.strip() for x in f.readlines()]

	score_table = {
	'(': 1,
	'[': 2,
	'{': 3,
	'<': 4
	}

	pairs = {
	')': '(',
	']': '[',
	'}': '{',
	'>': '<' 
	}

	score = []
	incomplete = []
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
				flag = False
				break
		if flag:
			incomplete.append(chunk_opener)

scores = []
for line in incomplete:
	score = 0
	line.reverse()
	for c in line:
		score *= 5
		score += score_table[c]
	scores.append(score)

scores.sort()
n = int(len(scores)/2)   

print(scores[n])

