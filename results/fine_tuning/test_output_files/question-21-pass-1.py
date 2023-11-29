spf = [0 for i in range(10001)]


def spf_array(spf):
    for i in range(1, 10001):
        if (spf[i] == 0):
            spf[i] = i
        while (i % spf[i] == 0):
            spf[i] = spf[i] * (spf[i] / i)
        i = spf[i]


def prime_factors(arr, n, k):
    spf_array(spf)
    for i in range(n):
        if (spf[arr[i]] % k == 0):
            print("Yes")
            return
    print("No")


arr = [1, 2, 3, 4, 5, 6]
n = 6
k = 3
prime_factors(arr, n, k)
