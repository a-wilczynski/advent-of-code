from copy import deepcopy

laternfishes = [0,0,0,0,0,0,0,0]

with open('testinput.txt') as f:
	initial = [int(x) for x in f.read().split(',')]
	print(initial)

	for i in initial:
		laternfishes[i] += 1

	print(laternfishes)



		


