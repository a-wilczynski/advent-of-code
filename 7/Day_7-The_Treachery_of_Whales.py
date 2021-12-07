with open('input.txt') as f:
	input_ = f.read()
	input_cleared = [int(x) for x in input_.split(',')]
	print(input_cleared)

	fuel = []
	for i in range(min(input_cleared),max(input_cleared) + 1):
		fuel.append(sum([abs(i-j) for j in input_cleared]))

	print(min(fuel))