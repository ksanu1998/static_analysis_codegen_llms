def checkSpecialPrime(sieve, num):

def checkSpecialPrime(sieve, num):
    # Initialize the smallest special prime as the number itself
    smallest_prime = num

    # Iterate over the sieve
    for i in range(num, len(sieve)):
        # Check if the current number is a prime number
        if sieve[i] == 1:
            # If the current number is a prime number, check if it is a special prime
            if isSpecialPrime(i, num):
                # If the current number is a special prime, return it
                return i

    # If no special prime greater than or equal to the given number is found, return -1
    return -1

def isSpecialPrime(num, base):
    # Check if the number is divisible by the base
    if num % base == 0:
        # If the number is divisible by the base, it is not a special prime
        return False

    # Check if the number is divisible by any of the prime factors of the base
    for i in range(2, base):
        if num % i == 0:
            # If the number is divisible by any of the prime factors of the base, it is not a special prime
            return False

    # If the number is not divisible by the base or any of its prime factors, it is a special prime
    return True
