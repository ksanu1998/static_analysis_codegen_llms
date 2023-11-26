import random
a, b = None, None


def partition(arr, l, r):
    i = random.randint(l, r)
    arr[i], arr[r] = arr[r], arr[i]
    pivot = arr[r]
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[j], arr[l] = arr[l], arr[j]
            l += 1
    arr[l], arr[r] = arr[r], arr[l]
    return l
