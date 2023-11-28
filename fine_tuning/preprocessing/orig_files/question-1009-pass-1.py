from math import log2


def minDistance(n1, n2):
    bitCount1 = int(log2(n1)) + 1
    bitCount2 = int(log2(n2)) + 1
    bitDiff = abs(bitCount1 - bitCount2)
    maxBitCount = max(bitCount1, bitCount2)
    if (bitCount1 > bitCount2):
        n2 = int(n2 * pow(2, bitDiff))
    else:
        n1 = int(n1 * pow(2, bitDiff))
    xorValue = n1 ^ n2
    if xorValue == 0:
        bitCountXorValue = 1
    else:
        bitCountXorValue = int(log2(xorValue)) + 1
    disSimilarBitPosition = (maxBitCount - bitCountXorValue)
    result = (bitCount1 + bitCount2 - 2 * disSimilarBitPosition)
    return result


if __name__ == '__main__':
    n1 = 12
    n2 = 5
    print(minDistance(n1, n2))
