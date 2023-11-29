import sys


def CalculateDifference(arr, n):
    sum = 0
    for i in range(n):
        sum += arr[i]
    sum = abs(sum - (n * (n + 1) / 2));
    print(sum)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = 5
    CalculateDifference(arr, n)
