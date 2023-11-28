def sieve(prime, n):
    # Create a list to store the prime numbers
    prime_list = []

    # Iterate through the range of numbers
    for i in range(2, n+1):
        # Check if the number is prime
        if i in prime:
            # Add the prime number to the list
            prime_list.append(i)

    # Return the list of prime numbers
    return prime_list
