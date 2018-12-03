with open("./input.txt", "r") as inputFile:
	lines = list(map(lambda x: x.strip(), inputFile.readlines()))

for x in range(0, len(lines)):
	line = lines[x]
	#print("main comparison: %s" % line)

	for y in range(x, len(lines)):
		test = lines[y]
		#print("with: %s" % test)
		if line == test:
			continue

		differ = 0
		for a in range(0, len(line)):
			if line[a] != test[a]:
				differ += 1

		if differ == 1:
			print("%s and %s might be an answer?" % (line, test))

		# i could programatically find the answer OR i can just look at it
		# pbykrmjmizwhxlqnmasfgtycdv
		# pbykrmjmizwhxlqnwasfgtycdv
		#                 *
		# pbykrmjmizwhxlqnasfgtycdv