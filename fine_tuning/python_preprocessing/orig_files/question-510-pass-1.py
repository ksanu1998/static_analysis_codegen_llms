def minFlips(target):
    curr = '1'
    count = 0
    for i in range(len(target)):
        if (target[i] == curr):
            count += 1
            curr = chr(48 + (ord(curr) + 1) % 2)
    return count


if __name__ == "__main__":
    S = "011000"
    print(minFlips(S))
