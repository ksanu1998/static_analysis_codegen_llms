# Split N natural numbers into two sets having GCD of their sums greater than 1. 
def createSets(N): 

	# Create an array to store the numbers 
	arr = [0]*N 

	# Initialize the numbers 
	for i in range(N): 
		arr[i] = i+1

	# Initialize the result 
	result = [] 

	# Initialize the sum of the numbers 
	sum = 0

	# Initialize the GCD of the numbers 
	gcd = 1

	# Initialize the count of numbers 
	count = 0

	# Initialize the index 
	index = 0

	# Traverse the array 
	while index < N: 

		# If the number is not visited 
		if arr[index]!= 0: 

			# Add the number to the result 
			result.append(arr[index]) 

			# Increment the count 
			count += 1

			# Update the sum 
			sum += arr[index] 

			# Update the GCD 
			gcd = gcd_of_two_numbers(gcd, arr[index]) 

			# Mark the number as visited 
			arr[index] = 0

			# If the count is equal to N 
			if count == N: 

				# If the sum is not divisible by GCD 
				if sum % gcd!= 0: 

					# Update the result 
					result = [] 

					# Initialize the count 
					count = 0

					# Initialize the sum 
					sum = 0

					# Initialize the GCD 
					gcd = 1

					# Initialize the index 
					index = 0

				# Else, if the sum is divisible by GCD