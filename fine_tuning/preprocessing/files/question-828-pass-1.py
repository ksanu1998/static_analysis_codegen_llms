def constructBlanceArray(BOP, BCP, str, n):
    balance = [0] * n
    for i in range(n):
        if BOP[i] == "(":
            balance[i] = 1
        elif BCP[i] == ")":
            balance[i] = -1
        else:
            balance[i] = 0
    return balance
