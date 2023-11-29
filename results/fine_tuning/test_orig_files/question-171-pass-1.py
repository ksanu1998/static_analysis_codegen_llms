def SumofInverseDivisors(N, Sum):

def SumofInverseDivisors(N, Sum):
    # Initialize the sum to 0
    sum = 0

    # Loop through all positive integers up to the square root of N
    for i in range(1, int(N ** 0.5) + 1):
        # If i is a divisor of N
        if N % i == 0:
            # Add the inverse of i to the sum
            sum += 1 / i

    # If the sum of the divisors is equal to the given Sum
    if sum == Sum:
        # Return the number N
        return N
    else:
        # If the sum of the divisors is not equal to the given Sum
        # Return -1 to indicate that no number has the given sum of inverse divisors
        return -1
