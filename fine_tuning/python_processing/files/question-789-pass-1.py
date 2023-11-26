def calculateSpan(price, n, S):
    span = 1
    for i in range(1, n):
        if price[i] > price[i-1]:
            span += 1
        S.append(span)
    return S
