N = 2


def isVowel(ch):
    return (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u')


def countVowels(string, l, r):
    cnt = 0
    for i in range(l, r + 1):
        if (isVowel(string[i])):
            cnt += 1
    return cnt


def performQueries(string, queries, q):
    for i in range(q):
        print(countVowels(string, queries[i][0], queries[i][1]))


if __name__ == "__main__":
    string = "geeksforgeeks"
    queries = [[1, 3], [2, 4], [1, 9]]
    q = len(queries)
    performQueries(string, queries, q)
