def CountOfTriplets(a, n):
    answer = 0
    x = 0
    count = [0 for i in range(100005)]
    ways = [0 for i in range(100005)]
    for i in range(n):
        x ^= a[i]
        answer += count[x] * i - ways[x]
        count[x] += 1
        ways[x] += (i + 1)
    return answer


if __name__ == '__main__':
    Arr = [3, 6, 12, 8, 6, 2, 1, 5]
    N = len(Arr)
    print(CountOfTriplets(Arr, N))
