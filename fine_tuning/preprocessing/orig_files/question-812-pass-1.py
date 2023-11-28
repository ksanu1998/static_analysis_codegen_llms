from collections import deque


def getIndex(s, i):
    if s[i] != '[':
        return -1
    d = deque()
    for k in range(i, len(s)):
        if s[k] == '[':
            d .append(s[i])
        elif s[k] == ']':
            d .popleft()
        if not d:
            return k
    return -1


def test(s, i):
    matching_index = getIndex(s, i)
    print(s + ", " + str(i) + ": " + str(matching_index))


def main():
    test("[ABC[23]][89]", 0)
    test("[ABC[23]][89]", 4)
    test("[ABC[23]][89]", 9)
    test("[ABC[23]][89]", 1)


if __name__ == "__main__":
    main()
