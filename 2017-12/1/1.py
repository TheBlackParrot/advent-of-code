with open("./input.txt", "r") as inputFile:
	lines = list(map(lambda x: x.strip(), inputFile.readlines()))

total = 0
for x in range(0, len(lines[0])):
	c = lines[0][x]
	try:
		n = lines[0][x+1]
	except:
		n = lines[0][0]

	if c == n:
		total += int(c)

print(total)