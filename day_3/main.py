def bin_to_int(str):
	return int(str, 2)

def get_bits_in_column(arr, col_num):
	bits = []
	for a in arr:
		bits.append(a[i])

	return bits

if __name__ == "__main__":
	with open("input.txt", "r") as f:
		readings = f.read().split("\n")

	gamma = ""
	epsilon = ""
	
	oxygen_readings = readings
	co2_readings = readings

	for i in range(len(readings[0])):
		bits = get_bits_in_column(readings, i)
		if bits.count('1') > bits.count('0'):
			gamma += "1"
			epsilon += "0"
		else:
			gamma += "0"
			epsilon += "1"

	for i in range(len(readings[0])):
		if len(oxygen_readings) == 1:
			break

		bits = bits = get_bits_in_column(oxygen_readings, i)
		if bits.count('1') >= bits.count('0'):
			oxygen_readings = [r for r in oxygen_readings if r[i] == '1']
		else:
			oxygen_readings = [r for r in oxygen_readings if r[i] == '0']

	for i in range(len(readings[0])):
		if len(co2_readings) == 1:
			break

		bits = get_bits_in_column(co2_readings, i)
		if bits.count('1') >= bits.count('0'):
			co2_readings = [r for r in co2_readings if r[i] == '0']
		else:
			co2_readings = [r for r in co2_readings if r[i] == '1']


	gamma = bin_to_int(gamma)
	epsilon = bin_to_int(epsilon)
	print(f"Result for Part 1: {gamma * epsilon}")

	oxygen_reading = bin_to_int(oxygen_readings[0])
	co2_reading = bin_to_int(co2_readings[0])
	print(f"Result for Part 2: {oxygen_reading * co2_reading}")

