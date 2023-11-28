def solve(arr, n):

def solve(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                count += 1
    return count
