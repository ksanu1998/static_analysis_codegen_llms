def func(n, m, A):
    ModArray = [0] * n
    Sum = 0
    for i in range(n):
        ModArray[i] = A[i] % m
        Sum += ModArray[i]
    Sum = Sum % m
    if (Sum % m == 0):
        print("True")
        return
    if (Sum % 2 != 0):
        print("False")
    else:
        ModArray .pop(0)
        i = 0
        j = len(ModArray) - 1
        ModArray .sort()
        Sum = Sum // 2
        while (i <= j):
            s = ModArray[i] + ModArray[j]
            if (s == Sum):
                i1 = i
                i2 = j
                print("True")
                break
            elif (s > Sum):
                j -= 1
            else:
                i += 1


m = 2
a = [1, 3, 9]
n = len(a)
func(n, m, a)
