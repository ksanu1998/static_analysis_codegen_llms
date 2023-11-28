def smallerNumbers(arr, N):
    hash = [0] * 100000
    for i in range(N):
        hash[arr[i]] += 1
    sum = 0
    for i in range(1, 100000):
        hash[i] += hash[i - 1]
    for i in range(N):
        if (arr[i] == 0):
            print("0")
            continue
        print(hash[arr[i] - 1], end=" ")


if __name__ == "__main__":
    arr = [3, 4, 1, 1, 2]
    N = len(arr)
    smallerNumbers(arr, N)
