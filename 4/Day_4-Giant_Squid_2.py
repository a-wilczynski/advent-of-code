def get_boards_and_key(raw_input):
	input_splitted = raw_input.split('\n\n')
	key = input_splitted[0].split(',')
	boards = []

	for i in input_splitted[1:]:
		temp = []
		for j in i.split("\n"): 
			k = j.split()
			temp.append(k)
		boards.append(temp)

	boards[-1].pop(-1)

	return key, boards

def check_number(number, boards):
	for i, board in enumerate(boards):
		for j, row in enumerate(board):
			for k, el in enumerate(row):
				if el == number:
					boards[i][j][k] = 'X'

def check_win(boards):
	for board in boards:
		inverted = list(zip(*board))

		if any(all(el == 'X' for el in row) for b in [board,inverted] for row in b):
			return board
	return False


def calculate(n, board):
	return sum(int(el) for row in board for el in row if el != 'X') * int(n)

with open('input.txt') as f:

	input_ = f.read()
	key, boards = get_boards_and_key(input_)

	for n in key:
		check_number(n,boards)

		while True:
			winner = check_win(boards)
			if winner:
				print(len(boards))
				if len(boards) == 1:
					print(calculate(n,winner))
				boards.remove(winner)
			else:
				break

		print(len(boards))


