import math
sub = [0 for i in range(100005)]



def minDivisorDifference(n):
    # Initialize the minimum difference between the divisors of two nodes
    min_diff = float('inf')

    # Loop through all possible pairs of nodes
    for i in range(1, n):
        for j in range(i+1, n):
            # Calculate the divisors of nodes i and j
            div_i = [x for x in range(1, int(math.sqrt(i))+1) if i % x == 0]
            div_j = [x for x in range(1, int(math.sqrt(j))+1) if j % x == 0]

            # Calculate the minimum difference between the divisors of nodes i and j
            diff = abs(len(div_i) - len(div_j))

            # Update the minimum difference if necessary
            if diff < min_diff:
                min_diff = diff

    return min_diff
