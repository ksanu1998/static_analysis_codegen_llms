def solve(a, n):
    # Create a new array to store the prefix sums
    prefix_sums = [0] * (n + 1)

    # Calculate the prefix sums of the input array
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + a[i]

    # Find the maximum number of primes in the prefix sums
    max_primes = 0
    for i in range(n + 1):
        if is_prime(prefix_sums[i]):
            max_primes += 1

    return max_primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True