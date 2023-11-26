def possibleToSort(arr, n, str):
    max_element = -1
    for i in range(len(str)):
        max_element = max(max_element, arr[i])
        if (str[i] == '0'):
            if (max_element > i + 1):
                return "No"
    return "Yes"


if __name__ == "__main__":
    arr = [1, 2, 5, 3, 4, 6]
    n = len(arr)
    str = "01110"
    print(possibleToSort(arr, n, str))
