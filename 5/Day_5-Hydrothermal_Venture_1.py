"""
1 . .  2 . .  
. . .  . . .
. . 2  . . 1

. . 1  . . 2
. . .  . . .
2 . .  1 . .


[1,1] [3,3] -> 2-1 [+,+]
[3,3] [1,1] -> 2-1 [-,-]
[1,3] [3,1] -> 2-1 [+,-]
[3,1] [1,3] -> 2-1 [-,+]

"""

def shuffle(coordinates):
	"""
	Coordinates are in form [[x1,y1],[x2,y2]].
	There are 4 cases of possible coordinates for 45 degree line

	1. [x1,y1] <- low left corner [x2,y2] <- high right corner
	2. [x1,y1] <- high righ corner [x2,y2] <- low left corner
	3. [x1,y1] <- high left corner [x2,y2] <- low right corner
	4. [x1,y1] <- low right corner [x2,y2] <- high left corner

	This function reduces those 4 cases to only two cases (1,3)

	"""
	if (coordinates[0][0] == coordinates[1][0]) or (coordinates[0][1] == coordinates[1][1]):
		return coordinates 
	if (coordinates[0][0] < coordinates[1][0]) and (coordinates[0][1] < coordinates[1][1]):
		return coordinates
	
	if (coordinates[0][0] > coordinates[1][0]) and (coordinates[0][1] > coordinates[1][1]):
		return [coordinates[1],coordinates[0]]

	if (coordinates[0][0] < coordinates[1][0]) and (coordinates[0][1] > coordinates[1][1]):
		return coordinates
	
	if (coordinates[0][0] > coordinates[1][0]) and (coordinates[0][1] < coordinates[1][1]):
		return [coordinates[1],coordinates[0]]



print(shuffle([[1,1],[3,3]]))
print(shuffle([[3,3],[1,1]]))
print(shuffle([[1,3],[3,1]]))
print(shuffle([[3,1],[1,3]]))
input()






def check_line(coordinates):
	"""
	[
	[x1,y1],
	[x2,y2]
	]
	"""
	if (coordinates[0][0] == coordinates[1][0]) or (coordinates[0][1] == coordinates[1][1]):
		return True
	elif abs(coordinates[0][0]-coordinates[1][0]) == abs(coordinates[0][1]-coordinates[1][1]):
		return True
	else:
		return False

def create_field():
	return [[0]*1000 for i in range(1000)]

def print_field(field):

	for i in field:
		print('\n')
		for j in i:
			print(j, end = ' ')
	print("\n\n\n")

def modify_field(coordinates, field):
	"""
	coordinates:
	[
	[x1,y1],
	[x2,y2]
	]
	"""
	x1 = coordinates[0][0]
	x2 = coordinates[1][0]
	y1 = coordinates[0][1]
	y2 = coordinates[1][1]

	if x1 == x2:
		step = int((y2-y1)/abs(y2-y1))
		# print('step: ',step)
		# print_field(field)

		while True:
			# print_field(field)
			if y2 == y1:
				field[x1][y1] += 1
				break
			# print(x1,y1)
			field[x1][y1] += 1
			y1 += step

	elif y1 == y2:
		step = int((x2-x1)/abs(x2-x1))
		# print('step: ',step)
		# print_field(field)
		while True:
			# print_field(field)
			if x2 == x1:
				field[x1][y1] += 1
				break
			
			# print('field: ', field[x1][y1])
			field[x1][y1] += 1
			x1 += step

	elif abs(x1 - x2) == abs(y1 - y2):
		if x1 < x2 and y1 < y2:

			while True:
				if x1 == x2 and y1 == y2:
					field[x1][y1] += 1
					break

				field[x1][y1] += 1
				x1 += 1
				y1 += 1

		if x1 < x2 and y1 > y2:

			while True:
				if x1 == x2 and y1 == y2:
					field[x1][y1] += 1
					break

				field[x1][y1] += 1
				x1 += 1
				y1 -= 1

with open('input.txt') as f:

	input_ = f.readlines()
	input_cleared = [[[int(k.split(',')[0]), int(k.split(',')[1])]for k in j] for j in [i.strip('\n').split(' -> ') for i in input_]]
	field = create_field()

	# print(len(input_cleared))
	# print(len(input_))

	for line in input_cleared:
		if check_line(line):
			print(line, 'is true')
			modify_field(shuffle(line), field)
			
	n = 0
	for i in field:
		for j in i:
			if j >= 2:
				n += 1

	print(n)


