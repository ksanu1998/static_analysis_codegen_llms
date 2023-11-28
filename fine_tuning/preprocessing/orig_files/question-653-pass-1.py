def unique(s):
    st = ""
    length = len(s)
    for i in range(length):
        c = s[i]
        if c not in st:
            st += c
    return st


if __name__ == "__main__":
    s = "geeksforgeeks"
    print(unique(s))
