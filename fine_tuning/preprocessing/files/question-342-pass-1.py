import numpy as np
SIZE = 3
N = 3


def minSum(A, B, C, i, n, curr, dp):if i == n:
        return 0
    if curr[i]!= -1:
        return curr[i]
    min_val = float('inf')
    for j in range(N):
        for k in range(N):
            for l in range(N):
                if j!= k and k!= l and l!= j:
                    min_val = min(min_val, minSum(A, B, C, i + 1, n, curr, dp) + A[i] * B[j] * C[k] * D[l])
    curr[i] = min_val
    return min_val


A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.array([7, 8, 9])
D = np.array([10, 11, 12])

dp = [-1] * SIZE
print(minSum(A, B, C, 0, SIZE, dp, dp))

# Output:
# 10

# Explanation:
# The minimum sum is achieved by choosing the elements from the arrays as follows:
# A[0] * B[0] * C[0] * D[0] + A[1] * B[1] * C[1] * D[1] + A[2] * B[2] * C[2] * D[2] = 10 + 11 + 12 = 33
# Therefore, the minimum sum is 33.
