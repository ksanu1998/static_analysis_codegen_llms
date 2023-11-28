def largestNum(a, b):
    return a * (bool)(a // b) + b * (bool)(b // a)


a = 22
b = 1231
print(largestNum(a, b))
