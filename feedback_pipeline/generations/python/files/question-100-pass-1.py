from math import sqrt


def ArithmeticMean(A, B):# Calculate the arithmetic mean of the two numbers
    return (A + B) / 2


def HarmonicMean(A, B):[/INST]
    # Calculate the harmonic mean of the two numbers
    return 2 / (1/A + 1/B)


def find_means(arr):[/INST]
    # Initialize two empty lists to store the arithmetic and harmonic means
    arithmetic_means = []
    harmonic_means = []

    # Iterate over the array
    for i in range(len(arr)):
        # Calculate the arithmetic mean of the current number and the previous number
        arithmetic_mean = ArithmeticMean(arr[i], arr[i-1])
        # Calculate the harmonic mean of the current number and the previous number
        harmonic_mean = HarmonicMean(arr[i], arr[i-1])
        # Append the arithmetic mean to the list
        arithmetic_means.append(arithmetic_mean)
        # Append the harmonic mean to the list
        harmonic_means.append(harmonic_mean)

    # Return the lists of arithmetic and harmonic means
    return arithmetic_means, harmonic_means


def main():[/INST]
    # Test the function with the given array
    arr = [1, 2, 3, 4, 5]
    arithmetic_means, harmonic_means = find_means(arr)
    print("Arithmetic means:", arithmetic_means)
    print("Harmonic means:", harmonic_means)


if __name__ == "__main__":
    main()