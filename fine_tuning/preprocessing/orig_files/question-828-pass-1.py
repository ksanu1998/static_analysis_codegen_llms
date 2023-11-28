def constructBlanceArray(BOP, BCP, str, n):
    stk = []
    for i in range(n):
        if (str[i] == '('):
            stk .append(i)
        else:
            if (len(stk) != 0):
                BCP[i] = 1
                BOP[stk[-1]] = 1
                stk .pop()
            else:
                BCP[i] = 0
    for i in range(1, n):
        BCP[i] += BCP[i - 1]
        BOP[i] += BOP[i - 1]


def query(BOP, BCP, s, e):
    if (BOP[s - 1] == BOP[s]):
        return (BCP[e] - BOP[s]) * 2
    else:
        return (BCP[e] - BOP[s] + 1) * 2


if __name__ == '__main__':
    string = "())(())(())("
    n = len(string)
    BCP = [0 for i in range(n + 1)]
    BOP = [0 for i in range(n + 1)]
    constructBlanceArray(BOP, BCP, string, n)
    startIndex = 5
    endIndex = 11
    print("Maximum Length Correct " +
          "Bracket Subsequence between " +
          str(startIndex) +
          " and " +
          str(endIndex) +
          " = " +
          str(query(BOP, BCP, startIndex, endIndex)))
    startIndex = 4
    endIndex = 5
    print("Maximum Length Correct " +
          "Bracket Subsequence between " +
          str(startIndex) +
          " and " +
          str(endIndex) +
          " = " +
          str(query(BOP, BCP, startIndex, endIndex)))
    startIndex = 1
    endIndex = 5
    print("Maximum Length Correct " +
          "Bracket Subsequence between " +
          str(startIndex) +
          " and " +
          str(endIndex) +
          " = " +
          str(query(BOP, BCP, startIndex, endIndex)))
