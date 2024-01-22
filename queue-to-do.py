def solution(start, length):
	result = 0
	x = 0
	y = 0
	for i in range(length):
		for j in range(length - i):
			result ^= start + j
		start += length

	return result

start_id = 1
line_length = 3
print("this is the solution", solution(start_id, line_length))