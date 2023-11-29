def solve(a, n):

def solve(a, n):
    # Sort the array in non-decreasing order
    a.sort()

    # Initialize the prefix sum array
    prefix_sum = [0] * (n + 1)

    # Compute the prefix sum of the array
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    # Initialize the maximum number of primes in the prefix sum
    max_primes = 0

    # Iterate over the prefix sum array
    for i in range(n + 1):
        # Check if the current prefix sum is prime
        if is_prime(prefix_sum[i]):
            # Increment the number of primes
            max_primes += 1

    # Return the maximum number of primes in the prefix sum
    return max_primes

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, n is not prime
                return False
        # If no divisor is found, n is prime
        return True
    else:
        # If n is less than or equal to 1, it is not prime
        return False
