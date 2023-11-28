def print_next_vovel_string(st):
    m = {}
    m['a'] = 0
    m['e'] = 1
    m['i'] = 2
    m['o'] = 3
    m['u'] = 4
    arr = ['a', 'e', 'i', 'o', 'u']
    N = len(st)
    for i in range(N):
        c = st[i]
        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
            index = m[st[i]] + 1
            newindex = index % 5
            st = st .replace(st[i], arr[newindex], 1)
    return st


if __name__ == "__main__":
    st = "geeksforgeeks"
    print(print_next_vovel_string(st))
