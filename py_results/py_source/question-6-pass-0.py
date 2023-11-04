# Count ways to place M objects in distinct partitions of N boxes. 
MOD = 1000000007


def power(x, y, p=MOD): 
    res = 1
    x = x % p 
    while (y > 0): 
        if (y & 1): 
            res = (res * x) % p 
        y = y >> 1
        x = (x * x) % p 
    return res 


def partition(n, m): 
    if (m == 1): 
        return 1
    if (n == m): 
        return 1
    if (n < m): 
        return 0
    return (partition(n - m, m) + partition(n, m - 1)) % MOD 


def main():
    n, m = map(int, input().split())
    print(power(partition(n, m), m))


if __name__ == '__main__':
    main()






































































































































































































































































