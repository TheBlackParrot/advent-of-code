with open("./input.txt", "r") as inputFile:
	lines = list(map(lambda x: x.strip(), inputFile.readlines()))

total = 0
half = int((len(lines[0])/2))

for x in range(0, len(lines[0])):
	c = lines[0][x]
	n = lines[0][(x + half) % len(lines[0])]

	if c == n:
		total += int(c)

print(total)