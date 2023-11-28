def countOddSum(a, n):
    c_odd = 0
    result = 0
    odd = False
    for i in range(n):
        if (a[i] % 2 == 1):
            if (odd):
                odd = False
            else:
                odd = True
        if (odd):
            c_odd += 1
    for i in range(n):
        result += c_odd
        if (a[i] % 2 == 1):
            c_odd = (n - i - c_odd)
    return result


if __name__ == '__main__':
    ar = [5, 4, 4, 5, 1, 3]
    n = len(ar)
    print("The Number of Subarrays" + "with odd sum is ", countOddSum(ar, n))
