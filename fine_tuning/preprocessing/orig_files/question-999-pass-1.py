def find_and(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans & arr[i]
    return ans


if __name__ == '__main__':
    arr = [1, 3, 5, 9, 11]
    print(find_and(arr))
