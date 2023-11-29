import math
sub = [0 for i in range(100005)]


def minDivisorDifference(n):
    for (i = 1; i <= n; i++)
        sub[i] = 1;
    for (i = 2; i <= n; i++)
        for (j = 1; j <= i / 2; j++)
            if (i % j == 0)
                sub[i] = (sub[i] + 1) % 2;
    ans = 0;
    for (i = 1; i <= n; i++)
        ans = (ans + (sub[i] * (n - i))) % 2;
    print(ans)
