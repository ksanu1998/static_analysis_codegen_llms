def solve(ang, n):

def solve(ang, n):
    # Initialize the number of occurrences to 0
    count = 0

    # Loop through each possible combination of 3 vertices
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # If the angle between the 3 vertices is ang, increment the count
                if abs(ang - (i - j - k)) % 360 == 0:
                    count += 1

    # Return the number of occurrences
    return count
