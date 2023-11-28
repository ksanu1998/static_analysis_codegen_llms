def maxbalancedprefix(str, n):
    _sum = 0
    maxi = 0
    for i in range(n):
        if str[i] == '(':
            _sum += 1
        else:
            _sum -= 1
        if _sum < 0:
            break
        if _sum == 0:
            maxi = i + 1
    return maxi


str = '((()())())(('
n = len(str)
print(maxbalancedprefix(str, n))
