def nextGreaterInLeft(a):
    n = len(a)
    res = 0
    for i in range(n-1):
        j = i+1
        while j < n:
            if a[j] > a[i]:
                res = max(res, a[i] * a[j])
                break
            j += 1
    return res
