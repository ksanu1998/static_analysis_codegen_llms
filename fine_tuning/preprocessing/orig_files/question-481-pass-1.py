def decHex(n):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    ans = ''
    while n:
        if n % 16 < 10:
            ans += str(n % 16)
        else:
            ans += alpha[n % 16 - 10]
        n //= 16
    ans = ans[::-1]
    return ans


def hexDec(convertedHex):
    mp = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    ans = 0
    pos = 0
    for i in convertedHex[::-1]:
        if i .isdigit():
            ans += (16 ** pos) * int(i)
        else:
            ans += (16 ** pos) * mp[i]
        pos += 1
    return ans


def removeChars(hexaVal, S):
    setk = set()
    for i in S:
        setk .add(i)
    ans = ''
    for i in hexaVal:
        if i in setk:
            continue
        ans += i
    return ans


def convertArr(arr, S):
    for i in range(len(arr)):
        hexaVal = decHex(arr[i])
        convertedHex = removeChars(hexaVal, S)
        decVal = hexDec(convertedHex)
        arr[i] = decVal
    print(arr)


arr = [74, 91, 31, 122]
S = "1AB"
convertArr(arr, S)
