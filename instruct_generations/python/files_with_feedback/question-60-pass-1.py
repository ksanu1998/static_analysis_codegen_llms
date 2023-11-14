import math



def divisorsSame(n):
    even_divisors = 0
    odd_divisors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                even_divisors += 1
            else:
                odd_divisors += 1
    return even_divisors == odd_divisors
