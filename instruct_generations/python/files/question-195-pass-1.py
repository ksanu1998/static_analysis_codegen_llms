max_Element = 100005
sum1 = [0 for i in range(max_Element)]
sum2 = [0 for i in range(max_Element)]
sum3 = [0 for i in range(max_Element)]


def precomputation(arr, n):
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i] == 0:
            for j in range(i * i, n + 1, i):
                arr[j] = 1