def check_directions(initial, field, y, x):
	"""Check directions that are possible to expand."""
	y_max = len(field)
	x_max = len(field[0])

	directions_all = [
		(y, x+1), # Right
		(y+1, x), # Down
		(y, x-1), # Left
		(y-1, x)  # Up
	]

	if initial in directions_all:
		directions_all.remove(initial)
	directions_possible = [d for d in directions_all if (0 <= d[0] < y_max) and (0 <= d[1] < x_max)]

	return directions_possible



def expand(initial, field, y, x):
	directions = check_directions(initial, field, y, x)
	size = 1
	field[y][x] = 9

	for d in directions:
		if field[d[0]][d[1]] != 9:
			size += expand((y,x), field, d[0], d[1])

	return size




with open('input.txt') as f:
	input_ = [list(map(lambda x: int(x), list(m))) for m in [n.strip('\n') for n in f.readlines()]]
	sizes = []
	for i in range(len(input_)):
		for j in range(len(input_[i])):
			if input_[i][j] != 9:
				size = expand((i,j), input_, i, j)
				sizes.append(size)
	
sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])


