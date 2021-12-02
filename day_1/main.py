def count_num_increases(measurements):
	num_increases = 0
	for i in range(len(measurements) - 1):
		if measurements[i + 1] > measurements[i]:
			num_increases += 1
	
	return num_increases


if __name__ == "__main__":
	with open("input.txt", "r") as f:
		measurements = [int(i) for i in f.read().split("\n")]

	print(f"Part A: Number of increases: {count_num_increases(measurements)}")

	filtered_measurements = [sum(measurements[i:i+3]) for i in range(len(measurements)- 2)]
	print(f"Part B: Number of increases: {count_num_increases(filtered_measurements)}")
