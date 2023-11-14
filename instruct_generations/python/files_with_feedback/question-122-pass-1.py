N = 100005
mod = (10 ** 9 + 7)
factorial = [0] * N
modinverse = [0] * N



def factorialfun():
    global factorial, mod
    factorial[0] = 1
    for i in range(1, N):
        factorial[i] = (factorial[i-1] * i) % mod
    return factorial
