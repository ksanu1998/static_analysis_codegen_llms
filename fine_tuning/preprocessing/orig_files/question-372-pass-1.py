dp = [[0 for i in range(1000)]for i in range(1000)]


def createPalindrome(input, isOdd):
    n = input
    palin = input
    if (isOdd):
        n //= 10
    while (n > 0):
        palin = palin * 10 + (n % 10)
        n //= 10
    return palin


def generatePalindromes(N):
    palindromes = []
    number = 0
    for j in range(2):
        i = 1
        number = createPalindrome(i, j)
        while number <= N:
            number = createPalindrome(i, j)
            palindromes .append(number)
            i += 1
    return palindromes


def minimumSubsetSize(A, i, j, N):
    if (not N):
        return 0
    if (i > j or A[i] > N):
        return 10 ** 9
    if (dp[i][N]):
        return dp[i][N]
    dp[i][N] = min(
        1 +
        minimumSubsetSize(
            A,
            i +
            1,
            j,
            N -
            A[i]),
        minimumSubsetSize(
            A,
            i +
            1,
            j,
            N))
    return dp[i][N]


def minimumNoOfPalindromes(N):
    palindromes = generatePalindromes(N)
    palindromes = sorted(palindromes)
    return minimumSubsetSize(palindromes, 0, len(palindromes) - 1, N)


N = 65
print(minimumNoOfPalindromes(N))
