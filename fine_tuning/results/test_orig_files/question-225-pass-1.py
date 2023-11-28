def isPossible(n, k, arr):

def isPossible(n, k, arr):
    # Initialize a dictionary to store the count of each element
    elem_count = {}
    # Loop through the array and increment the count of each element
    for i in range(len(arr)):
        if arr[i] in elem_count:
            elem_count[arr[i]] += 1
        else:
            elem_count[arr[i]] = 1
    # Check if all elements have the same count
    for i in range(n):
        if elem_count[i]!= k:
            return False
    return True
