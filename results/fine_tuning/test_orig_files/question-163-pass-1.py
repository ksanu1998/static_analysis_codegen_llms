def convert_To_Len_th_base(n, arr, Len, L):

def convert_To_Len_th_base(n, arr, Len, L):
    if L == 0:
        return []
    if n == 0:
        return [[]]
    result = []
    for i in range(Len):
        for j in convert_To_Len_th_base(n-arr[i], arr, Len, L-1):
            result.append([arr[i]] + j)
    return result
