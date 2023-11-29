def solve(ang, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if ang == abs(i - j) + abs(j - k) + abs(k - i):
                    count += 1
    return count
