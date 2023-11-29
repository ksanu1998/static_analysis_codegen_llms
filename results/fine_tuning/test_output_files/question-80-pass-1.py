def computePrime(N):
    isPrime[0] = 1
    for (i = 1; i <= N; i++)
        isPrime[i] = 1;
    for (i = 2; i <= N; i++)
        if (isPrime[i] == 1)
            for (j = i * i; j <= N; j += i)
                isPrime[j] = 0;
    for (i = 2; i <= N; i++)
        if (isPrime[i] == 1)
            for (j = i + 1; j <= N; j++)
                if (isPrime[j] == 1)
                    if (i % j == 0)
                        count++;
    return count;


if __name__ == "__main__":
    N = 10
    print(computePrime(N))
