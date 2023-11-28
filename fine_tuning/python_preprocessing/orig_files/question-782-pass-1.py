from copy import deepcopy
import math


def coprime(a, b):
    return (math .gcd(a, b)) == 1


def numOfPairs(arr, N):
    count = 0
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            if (coprime(int(arr[i]), int(arr[j]))):
                count = count + 1
    return count


def noOfCoPrimePairs(N, d1, d2):
    l = []
    l .append(str(d1))
    l .append(str(d2))
    l .sort()
    if int(N) < int(l[1]):
        return 0
    total = temp2 = deepcopy(l)
    flag = 0
    temp3 = []
    while len(l[0]) < 10:
        for i in range(len(l)):
            for j in range(2):
                if int(l[i] + temp2[j]) > int(N):
                    flag = 1
                    break
                total .append(l[i] + temp2[j])
                temp3 .append(l[i] + temp2[j])
            if flag == 1:
                break
        if flag == 1:
            break
        l = deepcopy(temp3)
        temp3 = []
    lenOfTotal = len(total)
    ans = numOfPairs(total, lenOfTotal)
    print(ans)


if __name__ == "__main__":
    N = 30
    d1 = 2
    d2 = 3
    noOfCoPrimePairs(N, d1, d2)
