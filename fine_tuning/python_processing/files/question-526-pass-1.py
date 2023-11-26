from math import floor


def jaro_distance(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0.0

    # Initialize the variables
    matches = 0
    m = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    # Loop through the characters of both strings
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i+1][j+1] = m[i][j] + 1
                matches += 1
            else:
                m[i+1][j+1] = max(m[i][j+1], m[i+1][j])

    # Calculate the Jaro distance
    p = (matches / len(s1)) + (matches / len(s2))
    return p - (m[len(s1)][len(s2)] / len(s1))
