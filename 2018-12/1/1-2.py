with open("./input.txt", "r") as inputFile:
	lines = list(map(lambda x: x.strip(), inputFile.readlines()))

iterations = 0
total = 0
seen = {}

while True:
	iterations += 1;
	print("iteration %i" % iterations)

	for line in lines:
		total += int(line)

		if total in seen:
			print("duplicate! %i" % total)
			exit();
		else:
			seen[total] = True