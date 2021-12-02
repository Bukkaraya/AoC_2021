if __name__ == "__main__":
	with open("input.txt", "r") as f:
		movements = f.read().split("\n")

	horizontal_pos = 0
	aim_based_depth = 0
	aim = 0

	for movement in movements:
		direction, steps = movement.split(" ")
		steps = int(steps)

		if direction == "forward":
			horizontal_pos += steps
			aim_based_depth += steps * aim
		elif direction == "down":
			aim += steps
		elif direction == "up":
			aim -= steps
	
	print(f"Result for Part 1: {horizontal_pos * aim}")
	print(f"Result for Part 2: {horizontal_pos * aim_based_depth}")