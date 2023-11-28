def oSRec(arr, i, j, Sum):
    if i > j:
        return 0
    if Sum == 0:
        return 1
    if arr[i] > Sum:
        return oSRec(arr, i+1, j, Sum)
    else:
        return oSRec(arr, i+1, j, Sum-arr[i]) + oSRec(arr, i+1, j, Sum)
