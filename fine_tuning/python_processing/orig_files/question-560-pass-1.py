def count_acronym(n, arr):
    freq = [0] * 26
    for i in range(n):
        freq[ord(arr[i][0]) - ord('a')] += 1
    cnt = 0
    for i in range(n):
        st = arr[i]
        num = [0] * 26
        for j in range(len(st)):
            num[ord(st[j]) - ord('a')] += 1
        flag = True
        for j in range(1, 26):
            if num[j] > freq[j]:
                flag = False
                break
        x = ord(st[0]) - ord('a')
        if freq[x] - 1 < num[x]:
            flag = False
        if flag:
            cnt += 1
    return cnt


if __name__ == "__main__":
    arr = ["abc", "bcad", "cabd", "cba", "dzzz"]
    n = 5
    print(count_acronym(n, arr))
