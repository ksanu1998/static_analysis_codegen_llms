def generate_derangement(N):
    def derangement(arr):
        if len(arr) == 1:
            return arr
        else:
            result = [arr[0]]
            for i in range(1, len(arr)):
                if arr[i]!= result[-1]:
                    result.append(arr[i])
            return result
    return derangement([i for i in range(1, N+1)])
