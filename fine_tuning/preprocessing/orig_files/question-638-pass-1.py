def query(s, i, j):
    n = len(s)
    i %= n
    j %= n
    print("Yes")if s[i] == s[j]else print("No")


if __name__ == "__main__":
    X = "geeksforgeeks"
    query(X, 0, 8)
    query(X, 8, 13)
    query(X, 6, 15)
