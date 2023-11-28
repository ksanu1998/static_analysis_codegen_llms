MOD = 1000000007


def FastDoubling(n, res):if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return (FastDoubling(n // 2, res) * FastDoubling(n // 2, res)) % MOD
    else:
        return (FastDoubling(n // 2, res) * FastDoubling(n // 2, res) * res) % MOD


def fibonacci(n):[/INST]
    res = 0
    return FastDoubling(n, res)


print(fibonacci(10))
