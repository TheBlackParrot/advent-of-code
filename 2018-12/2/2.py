with open("./input.txt", "r") as inputFile:
	lines = list(map(lambda x: x.strip(), inputFile.readlines()))

prod = [0, 0]
for line in lines:
	d = {}

	for char in line:
		if char not in d:
			d[char] = 0

		d[char] += 1

	checked2 = False
	checked3 = False
	for char in d:
		if d[char] == 2 and not checked2:
			prod[0] += 1
			checked2 = True
		elif d[char] == 3 and not checked3:
			prod[1] += 1
			checked3 = True

# where's my product() function >:(
print(prod[0] * prod[1])