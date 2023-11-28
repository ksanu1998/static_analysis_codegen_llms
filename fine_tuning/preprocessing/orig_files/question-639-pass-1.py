def countPairs(str1):
    result = 0
    n = len(str1)
    for i in range(0, n):
        for j in range(i + 1, n):
            if (abs(ord(str1[i]) - ord(str1[j])) == abs(i - j)):
                result += 1
    return result


if __name__ == "__main__":
    str1 = "geeksforgeeks"
    print(countPairs(str1))
