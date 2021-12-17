def increase_all(octo_table):
	for y in range(len(octo_table)):
		for x in range(len(octo_table[y])):
			octo_table[y][x] += 1

def increase_adjacent(octo_table, y, x):
	"""increase value of adjacent octopuses after flash"""
	coordinates = (
	(y, x+1),
	(y, x-1),
	(y+1, x),
	(y+1, x+1),
	(y+1, x-1),
	(y-1, x),
	(y-1, x+1),
	(y-1, x-1),
	)

	for c in coordinates:
		try:
			if octo_table[c[0]][c[1]] != 0 and c[0] >= 0 and c[1] >= 0:
				octo_table[c[0]][c[1]] += 1
		except:
			pass

def flash(octo_table):
	"""Make flash if octopus reache """
	flashed = False
	counter = 0

	for y, line in enumerate(octo_table):
		for x, octopus in enumerate(line):
			if octopus > 9:
				flashed = True
				counter += 1
				octo_table[y][x] = 0
				increase_adjacent(octo_table, y, x)
	if flashed:
		counter += flash(octo_table)

	return counter

def check_synchronized(octo_table):
	for i in octo_table:
		for j in i:
			if j != 0:
				return False
	return True

def print_table(octo_table):
	for i in octo_table:
		for j in i:
			print(j, end = ' ')
		print('\n')
	print('\n\n')





with open('input.txt') as f:
	input_ = []

	for line in f.readlines():
		input_.append([int(i) for i in line.strip()])
	score = 0 
	counter = 0 

	synchronized = False

	while True:
		if check_synchronized(input_):
			break
		increase_all(input_)
		score += flash(input_)
		counter += 1
		
	print(counter)
