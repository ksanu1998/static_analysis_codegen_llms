def removeConsecutiveSame(v):
    st = []
    for i in range(len(v)):
        if (len(st) == 0):
            st .append(v[i])
        else:
            Str = st[-1]
            if (Str == v[i]):
                st .pop()
            else:
                st .append(v[i])
    return len(st)


if __name__ == '__main__':
    V = ["ab", "aa", "aa", "bcd", "ab"]
    print(removeConsecutiveSame(V))
