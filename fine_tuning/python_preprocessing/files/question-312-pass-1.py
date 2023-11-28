def countSubsets(N):
    # Initialize the count array with all values as 1
    count = [1] * (N + 1)

    # Loop through the array and calculate the count of subsets
    # for each element
    for i in range(2, N + 1):
        for j in range(1, i):
            count[i] += count[j]

    return count[N]
