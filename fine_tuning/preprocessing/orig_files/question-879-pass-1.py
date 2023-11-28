def totalSumDivisibleByNum(digit, number):
    firstnum = pow(10, digit - 1)
    lastnum = pow(10, digit)
    firstnum = (firstnum - firstnum % number) + number
    lastnum = (lastnum - lastnum % number)
    count = ((lastnum - firstnum) / number + 1)
    return int(((lastnum + firstnum) * count) / 2)


digit = 3
num = 7
print(totalSumDivisibleByNum(digit, num))
