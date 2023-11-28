def countWays(s1, s2, n):
    count = 0
    for i in range(n):
        if s1[i]!= s2[i]:
            count += 1
    return count
