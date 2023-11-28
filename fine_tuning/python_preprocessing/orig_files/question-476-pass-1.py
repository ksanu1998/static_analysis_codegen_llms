def countSubstring(S, N):
    prevSum = {}
    res = 0
    currentSum = 0
    for i in range(N):
        if (S[i] >= 'A' and S[i] <= 'Z'):
            currentSum += 1
        else:
            currentSum -= 1
        if (currentSum == 0):
            res += 1
        if (currentSum in prevSum):
            res += (prevSum[currentSum])
        if currentSum in prevSum:
            prevSum[currentSum] += 1
        else:
            prevSum[currentSum] = 1
    return res


if __name__ == '__main__':
    S = "gEEk"
    print(countSubstring(S, len(S)))
