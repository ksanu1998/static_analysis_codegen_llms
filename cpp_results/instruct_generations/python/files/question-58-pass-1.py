import sys


def gcd(a, b):while b!= 0:
        a, b = b, a % b
    return a


def lcm(a, b):[/INST]
    return a * b // gcd(a, b)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    lcm_val = 1
    for i in range(n):
        for j in range(i + 1, n):
            lcm_val = lcm(lcm_val, arr[i] * arr[j])
    print(lcm_val)


if __name__ == "__main__":
    main()