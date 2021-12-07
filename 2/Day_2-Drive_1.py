import re
with open('input.txt') as f:
	input_ = f.read()
	
	forward = sum([int(n) for n in re.findall('forward (\d+)', input_)])
	down = sum([int(n) for n in re.findall('down (\d+)', input_)])
	up = sum([int(n) for n in re.findall('up (\d+)', input_)])

	print(f"forward: {forward}")
	print(f"down: {down}")
	print(f"up: {up}")
	print(f"forward * (down - up): {forward * (down-up)}")


