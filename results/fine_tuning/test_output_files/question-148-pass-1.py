def areAnagrams(a, b):
    n = len(a)
    if (n!= len(b)):
        print("Not Anagrams")
    else:
        c = 0
        for i in range(n):
            for j in range(n):
                if (a[i] == b[j]):
                    c += 1
        if (c == n):
            print("Anagrams")
        else:
            print("Not Anagrams")


if __name__ == "__main__":
    a = "abcd"
    b = "dcba"
    areAnagrams(a, b)
