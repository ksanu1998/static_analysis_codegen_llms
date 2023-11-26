def kthdigit(a, b, k):
    p = a ** b
    count = 0
    while (p > 0 and count < k):
        rem = p % 10
        count = count + 1
        if (count == k):
            return rem
        p = p / 10


a = 5
b = 2
k = 1
ans = kthdigit(a, b, k)
print(ans)
