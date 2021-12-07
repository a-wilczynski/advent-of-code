import re

depth = 0
aim = 0 
horizontal_position = 0

with open('input.txt') as f:
	diag = [list(map(lambda x: int(x), list((d.strip('\n'))))) for d in f.readlines()]
	sums = [sum(x) for x in list(zip(*diag))]
	gamma_rate_string = ''.join(['1' if s > 500 else '0' for s in sums])
	delta_rate_string = ''.join(['0' if x == '1' else '1' for x in gamma_rate_string])

	gamma_rate = int(gamma_rate_string,2)
	delta_rate = int(delta_rate_string,2)


	print(gamma_rate_string,delta_rate_string)
	print(gamma_rate * delta_rate)



