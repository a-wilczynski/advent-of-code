from copy import deepcopy

laternfishes = [0,0,0,0,0,0,0,0,0]

def reproduction(fishes):
	i = fishes.pop(0)
	fishes.append(i)
	fishes[6] += i



with open('input.txt') as f:
	initial = [int(x) for x in f.read().split(',')]
	print(initial)

	for i in initial:
		laternfishes[i] += 1

	for i in range(257):
		print(laternfishes, sum(laternfishes))
		reproduction(laternfishes)



		


