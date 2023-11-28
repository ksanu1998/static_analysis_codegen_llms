def count_carry(a, b):
    carry = 0
    count = 0
    len_a = len(a)
    len_b = len(b)
    while (len_a != 0 or len_b != 0):
        x = 0
        y = 0
        if (len_a > 0):
            x = int(a[len_a - 1]) + int('0')
            len_a -= 1
        if (len_b > 0):
            y = int(b[len_b - 1]) + int('0')
            len_b -= 1
        sum = x + y + carry
        if (sum >= 10):
            carry = 1
            count += 1
        else:
            carry = 0
    return count


a = "9555"
b = "555"
count = count_carry(a, b)
if (count == 0):
    print("0")
elif (count == 1):
    print("1")
else:
    print(count)
