def range_sum_query(S, Query):
    result = []
    for q in Query:
        start, end = q
        sum = 0
        for i in range(start, end):
            sum += S[i]
        result.append(sum)
    return result
