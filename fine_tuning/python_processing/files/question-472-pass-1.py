def find_min_inversion(n, s1, s2):
    # Initialize variables
    min_inversion = 0
    i = 0
    j = 0

    # Loop through the strings
    while i < n and j < n:
        # If the bits are equal, increment i and j
        if s1[i] == s2[j]:
            i += 1
            j += 1
        # If the bits are not equal, increment min_inversion and j
        else:
            min_inversion += 1
            j += 1

    # Return the minimum number of inversions required to make the strings equal
    return min_inversion
