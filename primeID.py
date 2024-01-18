def prime_string_creator():
	primes = ""
	num = 2

	while True:
		if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
			primes += str(num)
		if len(primes) >= 10005:
			break
		num += 1
	return	primes
    
    

def solution(n):
    primes = prime_string_creator()
    return primes[n:n+5]

print(solution(0))  # Output: "23571"
print(solution(3))  # Output: "71113"
print(int(2**0.5) + 1)
print(2 % 2)
if (2 % 2 != 0):
	print("what")