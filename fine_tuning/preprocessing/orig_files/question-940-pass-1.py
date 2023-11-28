def countXorPair(arr, n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if ((arr[i] ^ arr[j]) % 2 == 1):
                count += 1
    return count


if __name__ == "__main__":
    arr = [1, 2, 3]
    n = len(arr)
    print(countXorPair(arr, n))
