# Find prime factors of Array elements whose sum of exponents is divisible by K. 
spf = [0 for i in range(10001)]


def spf_array(spf): 
    for i in range(2, 10001): 
        if spf[i] == 0: 
            spf[i] = i 
            for j in range(i * i, 10001, i): 
                if spf[j] == j: 
                    spf[j] = i 
  
    return spf 


def prime_factors(n, spf): 
    prime_factors = [] 
    while (n > 1): 
        prime_factors.append(spf[n]) 
        n = n // spf[n] 
  
    return prime_factors 


def sum_of_exponents(n, spf): 
    sum_of_exponents = 0
    while (n > 1): 
        sum_of_exponents += spf[n] 
        n = n // spf[n] 
  
    return sum_of_exponents 


def find_prime_factors(arr, spf): 
    prime_factors = [] 
    for i in range(len(arr)): 
        prime_factors.append(prime_factors(arr[i], spf)) 
  
    return prime_factors 


def find_prime_factors_sum_of_exponents(arr, spf): 
    prime_factors_sum_of_exponents = [] 
    for i in range(len(arr)): 
        prime_factors_sum_of_exponents.append(sum_of_exponents(arr[i], spf)) 
  
    return prime_factors_sum_of_exponents 


def find_prime_factors_sum_of_exponents_divisible_by_k(arr, spf, k): 
    prime_factors_sum_of_exponents_divisible_by