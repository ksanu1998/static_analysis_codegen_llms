def sumOfSubstrings(num):
    sum = 0
    mf = 1
       for i in range(len(num) - 1, -1, -1):
            sum = sum + (int(num[i])) * (i + 1) * mf
            mf = mf * 10 + 1
        return sum


if __name__ == '__main__':
    num = "6759"
    print(sumOfSubstrings(num))
