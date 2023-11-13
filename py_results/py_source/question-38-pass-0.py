# Honaker Prime Number. 
limit = 10000000
position = [0] * (limit + 1)


def sieve(): 
    for i in range(2, limit): 
        if position[i] == 0: 
            for j in range(i * i, limit + 1, i): 
                position[j] = 1


def isPrime(n): 
    if n <= 1: 
        return False
    if n <= limit: 
        return position[n] == 0
    else: 
        for i in range(2, int(n ** 0.5) + 1): 
            if n % i == 0: 
                return False
        return True


def main():
    sieve()
    for i in range(2, limit):
        if isPrime(i):
            print(i)


if __name__ == "__main__":
    main()


# 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000