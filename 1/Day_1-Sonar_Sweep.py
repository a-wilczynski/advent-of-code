with open('input.txt') as f:
	input_ = f.readlines()
	deepths = [int(deepth.strip('\n')) for deepth in input_]
	counter = 0

	for n in range(1,len(deepths)):
		difference = deepths[n] - deepths[n-1]
		if difference > 0:
			print(f"deepth increased by {difference} ({deepths[n-1]} -> {deepths[n]})")
			counter += 1



	print(counter)