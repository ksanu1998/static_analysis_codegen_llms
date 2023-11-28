def reverse(string, length, l, r):
    if (l < 0 or r >= length or l > r):
        return string
    string = list(string)
    while (l < r):
        c = string[l]
        string[l] = string[r]
        string[r] = c
        l += 1
        r -= 1
    return "".join(string)


if __name__ == "__main__":
    string = "geeksforgeeks"
    length = len(string)
    l = 5
    r = 7
    print(reverse(string, length, l, r))
