def powerfulIntegers(x, y, bound):

def powerfulIntegers(x, y, bound):
    integers = set()
    for i in range(1, bound + 1):
        num = i
        while num <= bound:
            integers.add(num)
            num = num * x + y
    return list(integers)
