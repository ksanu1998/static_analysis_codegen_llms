def convert(n, a, b):
    result = ""
    for i in range(n):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result
