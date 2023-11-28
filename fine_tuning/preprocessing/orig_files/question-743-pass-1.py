import sys


def isPossible(arr, n):
    mini = sys .maxsize
    for i in range(n):
        mini = min(mini, arr[i])
    for i in range(n):
        if (arr[i] == mini):
            continue
        Max = (arr[i] + 1) // 2 - 1
        if (mini < 0 or mini > Max):
            return "No"
    return "Yes"


if __name__ == '__main__':
    arr = [1, 1, 3, 4]
    N = len(arr)
    print(isPossible(arr, N))
