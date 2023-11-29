def isTriPerfect(n):

def isTriPerfect(n):
    # Find the sum of the factors of n
    sum_of_factors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_of_factors += i
    # Check if the sum is equal to n
    return sum_of_factors == n
