def findMinLength(arr, n):
    min = len(arr[0])
    for i in range(1, n):
        if (len(arr[i]) < min):
            min = len(arr[i])
    return (min)


def commonPrefix(arr, n):
    minlen = findMinLength(arr, n)
    result = ""
    for i in range(minlen):
        current = arr[0][i]
        for j in range(1, n):
            if (arr[j][i] != current):
                return result
        result = result + current
    return (result)


if __name__ == "__main__":
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    n = len(arr)
    ans = commonPrefix(arr, n)
    if (len(ans)):
        print("The longest common prefix is ", ans)
    else:
        print("There is no common prefix")
