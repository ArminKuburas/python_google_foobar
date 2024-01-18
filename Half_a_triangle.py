def solution(x, y):
	worker_id = 1
	num = 1

	while x > 1:
		num += 1
		worker_id += num
		x -= 1
	while y > 1:
		worker_id += num
		num += 1
		y -= 1
	return str(worker_id)

# Example usage:
x = 3
y = 2
result = solution(x, y)
print(result)