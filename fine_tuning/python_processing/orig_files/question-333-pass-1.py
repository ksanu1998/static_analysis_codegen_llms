from itertools import permutations


def countWays(n):
    a = []
    i = 1
    while (i <= n):
        a .append(i)
        i += 1
    ways = 0
      flag = 1 if (per[0] == 1)else 0
       for i in range(1, n):
            if (abs(per[i] - per[i - 1]) > 2):
                flag = 0
        if (flag):
            ways += 1
    return ways
    for per in list(permutations(a)):


n = 6
print(countWays(n))
