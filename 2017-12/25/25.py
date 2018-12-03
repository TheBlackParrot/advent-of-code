string = "0"
position = 0

def start():
	string = "0"
	position = 0
	state = "A"
	direction = ""

	for step in range(0, 12964419):
		if state == "A":
			if string[position] == "0":
				string = string[:position] + '1' + string[position+1:]
				direction = "right"
				state = "B"
			else:
				string = string[:position] + '0' + string[position+1:]
				direction = "right"
				state = "F"

		elif state == "B":
			if string[position] == "0":
				string = string[:position] + '0' + string[position+1:]
				direction = "left"
				state = "B"
			else:
				string = string[:position] + '1' + string[position+1:]
				direction = "left"
				state = "C"

		elif state == "C":
			if string[position] == "0":
				string = string[:position] + '1' + string[position+1:]
				direction = "left"
				state = "D"
			else:
				string = string[:position] + '0' + string[position+1:]
				direction = "right"
				state = "C"

		elif state == "D":
			if string[position] == "0":
				string = string[:position] + '1' + string[position+1:]
				direction = "left"
				state = "E"
			else:
				string = string[:position] + '1' + string[position+1:]
				direction = "right"
				state = "A"

		elif state == "E":
			if string[position] == "0":
				string = string[:position] + '1' + string[position+1:]
				direction = "left"
				state = "F"
			else:
				string = string[:position] + '0' + string[position+1:]
				direction = "left"
				state = "D"

		elif state == "F":
			if string[position] == "0":
				string = string[:position] + '1' + string[position+1:]
				direction = "right"
				state = "A"
			else:
				string = string[:position] + '0' + string[position+1:]
				direction = "left"
				state = "E"

		if direction == "left":
			position -= 1

			if position < 0:
				string = "0%s" % string
				position = 0

		elif direction == "right":
			position += 1

			if position == len(string):
				string = "%s0" % string

	print(string.count('1'))

start()