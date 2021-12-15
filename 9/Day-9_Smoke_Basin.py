with open('input.txt') as f:
	input_ = [list(m) for m in [n.strip('\n') for n in f.readlines()]]
	print(input_)
	risk = 0

	for i in range(len(input_)):
		for j in range(len(input_[i])):

			center = input_[i][j]
			left = input_[i][j-1] if j > 0 else 10
			right = input_[i][j+1] if j < len(input_[i])-1 else 10
			up = input_[i-1][j] if i > 0 else 10
			down = input_[i+1][j] if i < len(input_)-1 else 10
			# print(i,j, range(len(input_)), range(i))
			# print(center, end = ' ')
			if int(center) < min(int(left), int(right), int(up), int(down)):
				risk += int(center) + 1

	print(risk)


