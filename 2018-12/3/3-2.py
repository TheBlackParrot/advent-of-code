with open("./input.txt", "r") as inputFile:
	lines = list(map(lambda x: x.strip(), inputFile.readlines()))

highestW = 0
highestL = 0

for line in lines:
	parts = line.split(" ")
	x, y = list(map(lambda x: int(x.strip(":")), parts[2].split(",")))
	w, l = list(map(lambda x: int(x), parts[3].split("x")))
	#print(w, l)

	if x+w > highestW:
		highestW = x+w
		print("highest width now %i" % highestW)
	if y+l > highestL:
		highestL = y+l
		print("highest length now %i" % highestL)

# grid = [[0]*highestW]*highestL <---- EVERYTHING IS A REFERENCE!!! BOOOO
grid = []
for x in range(0, highestW):
	grid.append([])
	for y in range(0, highestL):
		grid[x].append(0)

print(len(grid))
print(len(grid[0]))

for line in lines:
	# this is probably not the best method to just loop again but w/e
	parts = line.split(" ")
	x, y = list(map(lambda x: int(x.strip(":")), parts[2].split(",")))
	w, l = list(map(lambda x: int(x), parts[3].split("x")))

	# print("%i,%i: %ix%i" % (x, y, w, l))

	for a in range(x, x+w):
		for b in range(y, y+l):
			#print(a, b)
			grid[a][b] += 1

for line in lines:
	parts = line.split(" ")
	x, y = list(map(lambda x: int(x.strip(":")), parts[2].split(",")))
	w, l = list(map(lambda x: int(x), parts[3].split("x")))

	allOne = True
	for a in range(x, x+w):
		for b in range(y, y+l):
			if grid[a][b] != 1:
				allOne = False
				break

			if not allOne:
				continue

	if allOne:
		print("claim %s?" % parts[0])