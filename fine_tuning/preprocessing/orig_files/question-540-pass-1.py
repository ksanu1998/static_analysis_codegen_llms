def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def countStrings(string, n):
    distinct_char = set()
    for i in range(n):
        distinct_char .add(string[i])
    return fact(len(distinct_char))


if __name__ == "__main__":
    string = "geeksforgeeks"
    n = len(string)
    print(countStrings(string, n))
