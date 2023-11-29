def findUniqueElements(arr, N, K):

def findUniqueElements(arr, N, K):
    # Initialize a dictionary to store the count of each element
    count = {}
    
    # Loop through the array and increment the count of each element
    for i in range(N):
        if arr[i] in count:
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1
    
    # Find the element that occurs once
    for i in range(N):
        if count[arr[i]] == K:
            continue
        else:
            return arr[i]
