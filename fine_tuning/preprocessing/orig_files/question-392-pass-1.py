def chordCnt(A):
    n = 2 * A
    dpArray = [0] * (n + 1)
    dpArray[0] = 1
    dpArray[2] = 1
    for i in range(4, n + 1, 2):
        for j in range(0, i - 1, 2):
            dpArray[i] += (dpArray[j] * dpArray[i - 2 - j])
    return int(dpArray[n])


N = 2
print(chordCnt(N))
N = 1
print(chordCnt(N))
N = 4
print(chordCnt(N))
