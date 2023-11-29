def product_subarrays(arr, n):
    product = 1
    for (i, j) in product_subarrays_util(arr, n):
        product = (product * (j - i + 1))
    print(product)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    product_subarrays(arr, n)
