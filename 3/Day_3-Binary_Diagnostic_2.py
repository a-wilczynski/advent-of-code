import re
from copy import deepcopy	
from math import ceil

depth = 0
aim = 0 
horizontal_position = 0

with open('input.txt') as f:
	diag = [list(map(lambda x: int(x), list((d.strip('\n'))))) for d in f.readlines()]
	diag3 = deepcopy(diag)
	sums = [sum(x) for x in list(zip(*diag))]
	gamma_rate = [1 if s > 500 else 0 for s in sums]
	diag2 = deepcopy(diag)



	for i,n in enumerate(gamma_rate):
		diag = deepcopy(diag2)
		sums = [sum(x) for x in list(zip(*diag2))]
		diag_len = ceil(len(diag2)/2)
		gamma_rate = [1 if s >= diag_len else 0 for s in sums]

		d = 0
		for j,num in enumerate(diag):
			if num[i] != gamma_rate[i]:
				diag2.pop(j-d)
				d += 1
	x = diag2[0]

	diag2 = deepcopy(diag3)
	for i,n in enumerate(gamma_rate):
		diag = deepcopy(diag2)
		sums = [sum(x) for x in list(zip(*diag2))]
		diag_len = ceil(len(diag2)/2)
		gamma_rate = [0 if s >= diag_len else 1 for s in sums]

		d = 0
		for j,num in enumerate(diag):
			if num[i] != gamma_rate[i]:
				diag2.pop(j-d)
				d += 1
			if len(diag2) == 1:
				break
		if len(diag2) == 1:
			break

	y = diag2[0]

	x_str = [str(i) for i in x]
	y_str = [str(i) for i in y]

	print(int(''.join(x_str),2) * int(''.join(y_str),2))

