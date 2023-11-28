def sumOfDigits(N):
    sum = 0
    while (N):
        sum += (N % 10)
        N = N // 10
    return sum


def CountPair(arr, n):
    mp = {}
    for i in range(n):
        val = arr[i] + sumOfDigits(arr[i])
        if val in mp:
            mp[val] += 1
        else:
            mp[val] = 1
    count = 0
    for key, value in mp .items():
        val = key
        times = value
        count += ((times * (times - 1)) // 2)
    return count


if __name__ == '__main__':
    arr = [105, 96, 20, 2, 87, 96]
    N = len(arr)
    print(CountPair(arr, N))
