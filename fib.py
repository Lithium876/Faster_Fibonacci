'''
Making the Fibonacci Sequence faster and efficient
Using recursion and memoization 
'''

fibonacci_cache = dict()

def fibonacci(n):
	#Only want to key the most recent 100 values
	if len(fibonacci_cache) == 100:
		fibonacci_cache.clear()

	if n in fibonacci_cache:
		#Checking if the fibonacii of n is in fibonacci_cache
		return fibonacci_cache[n]
	if n == 1 or n == 2:
		return 1
	elif n > 2:
		value = fibonacci(n-1) + fibonacci(n-2)
		#make n the dictionary key and its fibonacci the value
		fibonacci_cache[n] = value
		return value

for i in range(1, 20):
	print(i,":",fibonacci(i))
