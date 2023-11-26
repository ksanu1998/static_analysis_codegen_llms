def oSRec(arr, i, j, Sum):
    if (j == i + 1):
        return max(arr[i], arr[j])
    return max(
        (Sum -
         oSRec(
             arr,
             i +
             1,
             j,
             Sum -
             arr[i])),
        (Sum -
         oSRec(
             arr,
             i,
             j -
             1,
             Sum -
             arr[j])))


def optimalStrategyOfGame(arr, n):
    Sum = 0
    Sum = sum(arr)
    return oSRec(arr, 0, n - 1, Sum)


arr1 = [8, 15, 3, 7]
n = len(arr1)
print(optimalStrategyOfGame(arr1, n))
arr2 = [2, 2, 2, 2]
n = len(arr2)
print(optimalStrategyOfGame(arr2, n))
arr3 = [20, 30, 2, 2, 2, 10]
n = len(arr3)
print(optimalStrategyOfGame(arr3, n))
