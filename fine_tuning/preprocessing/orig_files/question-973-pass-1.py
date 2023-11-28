def findNDigitNumsUtil(n, out, index, evenSum, oddSum):
    if (index > n):
        return
    if (index == n):
        if (abs(evenSum - oddSum) == 1):
            out[index] = ''
            out = ''.join(out)
            print(out, end=" ")
        return
    if (index & 1):
        for i in range(10):
            out[index] = chr(i + ord('0'))
            findNDigitNumsUtil(n, out, index + 1, evenSum, oddSum + i)
        for i in range(10):
            out[index] = chr(i + ord('0'))
            findNDigitNumsUtil(n, out, index + 1, evenSum + i, oddSum)


def findNDigitNums(n):
    out = [0] * (n + 1)
    index = 0
    evenSum = 0
    oddSum = 0
    for i in range(1, 10):
        out[index] = chr(i + ord('0'))
        findNDigitNumsUtil(n, out, index + 1, evenSum + i, oddSum)


if __name__ == "__main__":
    n = 3
    findNDigitNums(n)
