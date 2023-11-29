def isPossible(n, k, arr):
    # Initialize a dictionary to store the count of each element
    count = {}

    # Loop through the array and increment the count of each element
    for element in arr:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1

    # Check if it is possible to make all elements equal
    for element in count:
        if count[element] % k!= 0:
            return False

    return True
