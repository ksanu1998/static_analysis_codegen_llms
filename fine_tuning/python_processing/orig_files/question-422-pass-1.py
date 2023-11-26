def nCr(n, k):
    C = [[0 for i in range(k + 1)]for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if (j == 0 or j == i):
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]


def resultOfAllSubsets(arr, N):
    sum = 0
    for i in range(N):
        sum += arr[i]
    for n in range(1, N + 1):
        result += (sum * (nCr(N - 1, n - 1))) / n
    return result


arr = [2, 3, 5, 7]
N = len(arr)
print(resultOfAllSubsets(arr, N))
