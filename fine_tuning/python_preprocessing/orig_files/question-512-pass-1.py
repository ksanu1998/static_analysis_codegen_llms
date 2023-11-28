import sys
INT_MAX = sys .maxsize


def count_min_length(s):
    hash = [0] * 26
    ans = sys .maxsize
    for i in range(26):
        hash[i] = -1
    for i in range(len(s)):
        if (hash[ord(s[i]) - ord('a')] == -1):
            hash[ord(s[i]) - ord('a')] = i
        else:
            if (hash[ord(s[i]) - ord('a')] == i -
                    1 or hash[ord(s[i]) - ord('a')] == i - 2):
                return 0
            ans = min(ans, i - hash[ord(s[i]) - ord('a')] - 1)
            hash[ord(s[i]) - ord('a')] = i
    if (ans == INT_MAX):
        return -1
    return ans


if __name__ == "__main__":
    string = "abcdeba"
    print(count_min_length(string))
