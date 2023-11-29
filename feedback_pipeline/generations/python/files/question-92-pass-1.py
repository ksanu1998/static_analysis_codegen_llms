graph = [[]for i in range(100)]
weight = [0] * 100
ans = 0


def isPowerful(n):
    if n == 1:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True