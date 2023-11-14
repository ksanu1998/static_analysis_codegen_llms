def convert_to_len_th_base(n, arr, Len, L):
    if L == 0:
        return []
    elif n == 0:
        return [[]]
    else:
        result = []
        for i in range(len(arr)):
            for j in convert_to_len_th_base(n-arr[i], arr, Len, L-1):
                result.append([arr[i]] + j)
        return result
