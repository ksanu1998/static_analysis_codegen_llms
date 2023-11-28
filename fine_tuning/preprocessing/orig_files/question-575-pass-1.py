def StringMatch(S):
    lo, hi = 0, len(S)
    ans = []
    for x in S:
        if x == 'I':
            ans .append(lo)
            lo += 1
        else:
            ans .append(hi)
            hi -= 1
    return ans + [lo]


S = "IDID"
print(StringMatch(S))
