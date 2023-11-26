def nCycle(N):import math

def nCycle(N):
    return math.factorial(N) // (math.factorial(2) * math.factorial(N - 2))
