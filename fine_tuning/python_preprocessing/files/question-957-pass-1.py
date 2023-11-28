def nthPalindrome(n, k):
    if k == 1:
        return str(n)
    else:
        digits = [int(d) for d in str(n)]
        center = k // 2
        left = digits[:center]
        right = digits[center:]
        return "".join([str(d) for d in left + right])
