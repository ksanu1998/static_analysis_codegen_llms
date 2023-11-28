def calculateSpan(price, S):
    span = 1
    for i in range(1, len(S)):
        if price < S[i]:
            span += 1
    return span
