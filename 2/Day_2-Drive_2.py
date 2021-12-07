import re

depth = 0
aim = 0 
horizontal_position = 0

with open('input.txt') as f:
	input_ = f.read()
	operations = re.findall('(forward|down|up) (\d+)', input_)

	for o in operations:
		operation_name = o[0]
		unit = int(o[1])

		match operation_name:
			case 'forward':
				horizontal_position += unit
				depth += aim * unit
			case 'down':
				aim += unit
			case 'up':
				aim -= unit


	print(depth, aim, horizontal_position, depth*horizontal_position)




