def pairwiseDifference(arr, n):

def pairwiseDifference(arr, n):
    result = []
    for i in range(n-1):
        result.append(abs(arr[i] - arr[i+1]))
    return result
