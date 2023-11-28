def compute_hash(str):
    p = 31
    MOD = 10 ** 9 + 7
    hash_val = 0
    mul = 1
    for ch in str:
        hash_val = (hash_val + (ord(ch) - ord('a') + 1) * mul) % MOD
        mul = (mul * p) % MOD
    return hash_val


def distinct_str(arr, n):
    hash = [0] * (n)
    for i in range(n):
        hash[i] = compute_hash(arr[i])
    hash = sorted(hash)
    cntElem = 1
    for i in range(1, n):
        if (hash[i] != hash[i - 1]):
            cntElem += 1
    return cntElem


if __name__ == '__main__':
    arr = ["abcde", "abcce", "abcdf", "abcde"]
    N = len(arr)
    print(distinct_str(arr, N))
