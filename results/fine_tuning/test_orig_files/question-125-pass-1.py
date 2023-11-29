mod = 10 ** 9 + 7
N = 1000005
lpf = [0 for i in range(N)]



def least_prime_factor():
    lpf = [0] * N
    lpf[1] = 1
    for i in range(2, N):
        if lpf[i] == 0:
            lpf[i] = i
        for j in range(i * i, N, i):
            if lpf[j] == j:
                lpf[j] = i
    return lpf
