def longestString(str1, str2):
    count1 = [0] * 26
    count2 = [0] * 26
    for i in range(len(str1)):
        count1[ord(str1[i]) - ord('a')] += 1
    for i in range(len(str2)):
        count2[ord(str2[i]) - ord('a')] += 1
    result = ""
    for i in range(26):
        for j in range(1, min(count1[i], count2[i]) + 1):
            result = result + chr(ord('a') + i)
    print(result)


if __name__ == "__main__":
    str1 = "geeks"
    str2 = "cake"
    longestString(str1, str2)
