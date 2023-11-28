def possibleToSort(arr, n, str):
    # Check if the string is already sorted
    if str == "sorted":
        return True

    # Check if the string is already reversed
    if str == "reversed":
        return False

    # Check if the string is a permutation of the array
    perm = [0] * n
    for i in range(n):
        perm[arr[i] - 1] += 1
    for i in range(n):
        if perm[i]!= 1:
            return False
    return True
