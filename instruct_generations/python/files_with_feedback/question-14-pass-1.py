from math import sqrt, ceil, floor


def constructArrayWithGivenLCM(N):import math

def constructArrayWithGivenLCM(N):
    # Find the greatest common divisor of 1 to N
    gcd = math.gcd(N)

    # Calculate the least common multiple of 1 to N
    lcm = (N * gcd) // gcd

    # Construct the array by iterating from 1 to N
    arr = [i for i in range(1, N+1)]

    # Shuffle the array to create a random sequence
    random.shuffle(arr)

    # Return the first LCM elements of the shuffled array
    return arr[:lcm]
