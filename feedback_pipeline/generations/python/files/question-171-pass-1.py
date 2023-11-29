def SumofInverseDivisors(N, Sum):
    divisors = []
    for i in range(1, N + 1):
        if N % i == 0:
            divisors.append(i)
    return sum(1/i for i in divisors)