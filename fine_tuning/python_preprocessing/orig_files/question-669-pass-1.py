def firstDigit(n):
    while (n >= 10):
        n //= 10
    return n


def getCount(n):
    count = 1
    while (n != 0):
        leadDigit = firstDigit(n)
        n -= leadDigit
        count += 1
    return count


def getLargestNumber(k):
    left = k
    right = k * 10
    mid = (left + right) // 2
    length = getCount(mid)
    while (length != k):
        mid = (left + right) // 2
        length = getCount(mid)
        if (length > k):
            right = mid
        else:
            left = mid
    while (length == k):
        if (length != getCount(mid + 1)):
            break
        mid += 1
    return mid


if __name__ == "__main__":
    k = 3
    print(getLargestNumber(k))
