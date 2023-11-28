def alternatingSumOfFirst_N(N):

def alternatingSumOfFirst_N(N):
    return sum([-1] * (i % 2) for i in range(1, N + 1))
