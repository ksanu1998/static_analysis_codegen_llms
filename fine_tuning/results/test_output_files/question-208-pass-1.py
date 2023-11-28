import sys


def findMissingNums(even, sizeEven, odd, sizeOdd):
    evenSum = 0
    for i in range(sizeEven):
        evenSum += even[i]
    oddSum = 0
    for i in range(sizeOdd):
        oddSum += odd[i]
    if (evenSum - oddSum) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    even = [1, 2, 3, 4, 5]
    sizeEven = 5
    odd = [1, 2, 3, 4, 5]
    sizeOdd = 5
    findMissingNums(even, sizeEven, odd, sizeOdd)
