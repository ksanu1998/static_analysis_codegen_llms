def primeFactors(num):
    ans = dict()
    i = 2
    while (i * i <= num):
        while (num % i == 0):
            num //= i
            if i not in ans:
            ans[i] = 0
            ans[i] += 1
    if (num > 1):
    if num not in ans:
        ans[num] = 0
    ans[num] += 1
    return ans


def legendre(factor, num):
    count = 0
    fac2 = factor
    while (num >= factor):
        count += num // factor
        factor *= fac2
    return count


def possible(factors, num):
    for it in factors .keys():
        if (legendre(it, num) < factors[it]):
            return False
    return True


def search(start, end, factors):
    mid = (start + end) // 2
    if (not possible(factors, mid)):
        return search(mid + 1, end, factors)
    if (start == mid):
        return mid
    return search(start, mid, factors)


def findFact(num):
    factors = primeFactors(num)
    return search(1, num, factors)


if __name__ == '__main__':
    print(findFact(6))
    print(findFact(997587429953))
