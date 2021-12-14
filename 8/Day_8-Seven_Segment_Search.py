#		    0 1 2 3 4 5 6 7 8 9
segments = [6,2,5,5,4,5,6,3,7,6]

with open('input.txt') as f:
	input_raw = f.readlines()
	input_cleared = [[i.split(' | ')[0].split(), i.split(' | ')[1].strip('\n').split()] for i in input_raw]
	print(input_cleared[0])
	print(input_cleared[-1])

	counter = 0 

	for i in input_cleared:
		print(i)
		for j in i[1]:
			if len(j) in [2,4,3,7]:
				counter += 1
				print(j, len(j), counter)

	print(counter)