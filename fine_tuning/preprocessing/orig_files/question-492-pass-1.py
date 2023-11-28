combination = ""
combinations = []


def printSequences(combinations):
    for s in (combinations):
        print(s, end=' ')


def generateCombinations(s, n):
    global combination
    for i in range(len(s)):
        combination += s[i]
        x = int(combination)
        if (x <= n):
            combinations .append(combination)
            generateCombinations(s, n)
        combination = combination[:-1]


if __name__ == "__main__":
    S = "124"
    N = 100
    generateCombinations(S, N)
    printSequences(combinations)
