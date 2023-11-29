max_Element = 100005
sum1 = [0 for i in range(max_Element)]
sum2 = [0 for i in range(max_Element)]
sum3 = [0 for i in range(max_Element)]



def precomputation(arr, n):
    for i in range(2, n):
        if arr[i] == 0:
            continue
        for j in range(i, n):
            if arr[j] == 0:
                continue
            arr[i] = arr[i] * arr[j]
