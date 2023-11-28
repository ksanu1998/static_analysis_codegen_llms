def countSubStr(string, n):
    length = len(string)
    return (length - n + 1)


if __name__ == "__main__":
    string = "geeksforgeeks"
    n = 5
    print(countSubStr(string, n))
