#		    0 1 2 3 4 5 6 7 8 9
segments = [6,2,5,5,4,5,6,3,7,6]

with open('input.txt') as f:
	input_raw = f.readlines()
	input_cleared = [[i.split(' | ')[0].split(), i.split(' | ')[1].strip('\n').split()] for i in input_raw]

	"""
	1) Divide numbers into groups:
		[1, 4, 7, 8] <- unique numbers
		[0, 9, 6] 	 <- consists of 6 elements
		[2, 3, 5]    <- consists of 5 elements 

	2) in [0, 9, 6] group only number that doesn't have common two elements with "1" is "6"
	3) in [2, 3, 5] group only number that has common two elements with "1" is "3"
	4) in [0, 9] group only number that has common four elements with "4" is "9"
	5) in [2, 5] group only number that has common three elements with "4" is "5"
	6) all numbers are known 

	"""

	numbers = dict.fromkeys(list(range(10)))
	groups = {5: [], 6: []}
	output_sum = []

	for i in input_cleared:
		for j in i[0]:
			if len(j) == 5:
				groups[5].append(set(j)) 
			elif len(j) == 6:
				groups[6].append(set(j))
			elif len(j) == 2:
				numbers[1] = set(j)
			elif len(j) == 3:
				numbers[7] = set(j)
			elif len(j) == 4:
				numbers[4] = set(j)
			elif len(j) == 7:
				numbers[8] = set(j)

		numbers[6] = [n for n in groups[6] if len(numbers[1] & n) == 1][0]
		groups[6].remove(numbers[6])
		
		numbers[3] = [n for n in groups[5] if len(numbers[1] & n) == 2][0]
		groups[5].remove(numbers[3])

		numbers[9] = [n for n in groups[6] if len(numbers[4] & n) == 4][0]
		groups[6].remove(numbers[9])

		numbers[2] = [n for n in groups[5] if len(numbers[4] & n) == 2][0]
		groups[5].remove(numbers[2])

		numbers[0] = groups[6].pop()
		numbers[5] = groups[5].pop()


		output_number = []
		for j in i[1]:
			for k,v in numbers.items():
				if v == set(j):
					output_number.append(str(k))

		output_sum.append(int(''.join(output_number)))

		
	print(sum(output_sum))





