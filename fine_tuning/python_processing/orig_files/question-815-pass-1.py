def nextGreater(arr, n, next, order):
    S = []
    for i in range(n - 1, -1, -1):
        while (S != [] and (arr[S[len(S) - 1]] <= arr[i]
               if (order == 'G')else arr[S[len(S) - 1]] >= arr[i])):
            S .pop()
        if (S != []):
            next[i] = S[len(S) - 1]
        else:
            next[i] = -1
        S .append(i)


def nextSmallerOfNextGreater(arr, n):
    NG = [None] * n
    RS = [None] * n
    nextGreater(arr, n, NG, 'G')
    nextGreater(arr, n, RS, 'S')
    for i in range(n):
        if (NG[i] != -1 and RS[NG[i]] != -1):
            print(arr[RS[NG[i]]], end=" ")
        else:
            print("-1", end=" ")


if __name__ == "__main__":
    arr = [5, 1, 9, 2, 5, 1, 7]
    n = len(arr)
    nextSmallerOfNextGreater(arr, n)
