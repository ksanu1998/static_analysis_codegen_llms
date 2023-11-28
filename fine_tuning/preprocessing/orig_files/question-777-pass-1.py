import sys


def average(arr, N):
    sum = 0
    for i in range(N):
        sum += arr[i]
    return sum // N * 1.0 - 1


def mean(arr, N):
    avg = 0
    for i in range(N):
        avg += (arr[i] - avg) / (i + 1)
    return round(avg, 7)


if __name__ == '__main__':
    arr = [2147483647, 1, 2]
    N = len(arr)
    print("Average by Standard method: ",
          "{:.10f}".format(-1.0 * average(arr, N)))
    print("Average by Efficient method: ", "{:.10f}".format(mean(arr, N)))
