def longest_common_subsequence_with_permutations(str1, str2):
    # Create a 2D array to store the length of the longest common subsequence
    # for each position in str1 and str2
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # Fill in the first row and column with the lengths of the individual strings
    for i in range(1, len(str1) + 1):
        dp[i][0] = max(dp[i - 1][0], len(str1[i - 1]))
    for j in range(1, len(str2) + 1):
        dp[0][j] = max(dp[0][j - 1], len(str2[j - 1]))

    # Fill in the rest of the 2D array using the recurrence relation
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return the longest common subsequence
    return "".join(str1[i - 1] for i in range(dp[len(str1)][len(str2)], 0, -1) if dp[i][len(str2)] == dp[len(str1)][len(str2)])
