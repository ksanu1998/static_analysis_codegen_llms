from collections import defaultdict


def countPairs(arr, N):
    count = 0
    mp = defaultdict(int)
    for i in range(N):
        val = 1.0 * arr[i]
        idx = 1.0 * (i + 1)
        count += mp[val / idx]
        mp[val / idx] += 1
    print(count)


if __name__ == "__main__":
    arr = [1, 3, 5, 6, 5]
    N = len(arr)
    countPairs(arr, N)
