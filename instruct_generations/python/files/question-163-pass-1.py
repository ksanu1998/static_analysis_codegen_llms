def convert_To_Len_th_base(n, arr, Len, L):
    if L == 0:
        return []
    elif n == 0:
        return [[]]
    else:
        result = []
        for i in range(len(arr)):
            for j in convert_To_Len_th_base(n-arr[i], arr, Len, L-1):
                result.append([arr[i]] + j)
        return result