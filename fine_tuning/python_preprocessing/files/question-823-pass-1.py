st = []


def push_digits(number):// 'number' is a string
    for digit in number:
        st.append(int(digit))


def pop_digits(n):[/INST]
    // 'n' is the number of digits to pop
    result = 0
    for i in range(n):
        result = result * 10 + st.pop()
    return result


def reverse(number):[/INST]
    push_digits(number)
    result = pop_digits(len(number))
    return result


print(reverse("1234")) // should print 4321
print(reverse("-1234")) // should print -4321
print(reverse("123")) // should print 321
print(reverse("-123")) // should print -321
print(reverse("123456789")) // should print 987654321
print(reverse("-123456789")) // should print -987654321
print(reverse("")) // should print 0
print(reverse(" ")) // should print 0
print(reverse("   ")) // should print 0
print(reverse("123 456")) // should print 654321
print(reverse("123 456 ")) // should print 654321
print(reverse("123 456  ")) // should print 654321
print(reverse("123 456   ")) // should print 654321
print(reverse("123 456    ")) // should print 654321
print(reverse("123 456     ")) // should print 654
