def largestAnagramGrp(arr):
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
             43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    max = -1
    maxpdt = -1
    W = {}
    P = {}
    for temp in arr:
        c = [i for i in temp]
        pdt = 1
        for t in c:
            pdt *= prime[ord(t) - ord('a')]
        if (pdt in P):
            P[pdt] = P .get(pdt, 0) + 1
        else:
            W[pdt] = temp
            P[pdt] = 1
    for e in P:
        if (max < P[e]):
            max = P[e]
            maxpdt = e
    return W[maxpdt]


if __name__ == '__main__':
    S = "please be silent and listen to what the professor says"
    arr = S .split(" ")
    print(largestAnagramGrp(arr))
