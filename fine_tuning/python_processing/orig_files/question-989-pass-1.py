def nthMagicNo(n):
    pow = 1
    answer = 0
    while (n):
        pow = pow * 5
        if (n & 1):
            answer += pow
    return answer


n = 5
print("nth magic number is", nthMagicNo(n))
