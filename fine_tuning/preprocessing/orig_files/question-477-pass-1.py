def subString(s, n):
    count = 0
    for i in range(n):
        for len in range(i + 1, n + 1):
            test_str = (s[i:len])
            res = {}
            for keys in test_str:
                res[keys] = res .get(keys, 0) + 1
            flag = 0
            for keys in res:
                if res[keys] % 2 != 0:
                    flag = 1
                    break
            if flag == 0:
                count += 1
    return count


S = "abbaa"
N = len(S)
print(subString(S, N))
