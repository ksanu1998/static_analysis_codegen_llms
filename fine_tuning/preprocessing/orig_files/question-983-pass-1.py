def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print("true")if isPrime(11)else print("false")
print("true")if isPrime(14)else print("false")
