def countOfMultiples(n):
    return (int(n / 3) + int(n / 5) - int(n / 15))


print(countOfMultiples(6))
print(countOfMultiples(16))
