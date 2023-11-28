def smallestMaximum(N, K):
    sum = ((N + K - 1) // K) * K
    if (sum % N != 0):
        return (sum // N) + 1
    else:
        return sum // N


if __name__ == "__main__":
    N = 4
    K = 3
    print(smallestMaximum(N, K))
