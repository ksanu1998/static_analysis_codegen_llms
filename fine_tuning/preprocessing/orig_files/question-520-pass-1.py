def maxi(x, y):
    if x > y:
        return x
    else:
        return y


def longestPalindromic(strn, i, j, count):
    if i > j:
        return count
    if i == j:
        return (count + 1)
    if strn[i] == strn[j]:
        count = longestPalindromic(strn, i + 1, j - 1, count + 2)
        return maxi(
            count,
            maxi(
                longestPalindromic(
                    strn,
                    i + 1,
                    j,
                    0),
                longestPalindromic(
                    strn,
                    i,
                    j - 1,
                    0)))
    return maxi(
        longestPalindromic(
            strn,
            i + 1,
            j,
            0),
        longestPalindromic(
            strn,
            i,
            j - 1,
            0))


def longest_palindromic_substr(strn):
    k = len(strn) - 1
    return longestPalindromic(strn, 0, k, 0)


strn = "aaaabbaa"
print(longest_palindromic_substr(strn))
