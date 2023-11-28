def PartitionSub(arr, i, N, K, nos, v):
    if (i >= N):
        if (nos == K):
            for x in range(len(v)):
                print("{ ", end="")
                for y in range(len(v[x])):
                    print(v[x][y], end="")
                    if (y == len(v[x]) - 1):
                        print(" ", end="")
                    else:
                        print(", ", end="")
                if (x == len(v) - 1):
                    print("}", end="")
                else:
                    print("}, ", end="")
            print("",  end  = "")
        return
    for j in range(K):
        if (len(v[j]) > 0):
            v[j].append(arr[i])
            PartitionSub(arr, i + 1, N, K, nos, v)
            v[j].remove(v[j][len(v[j]) - 1])
        else:
            v[j].append(arr[i])
            PartitionSub(arr, i + 1, N, K, nos + 1, v)
            v[j].remove(v[j][len(v[j]) - 1])
            break


def partKSubsets(arr, N, K):
    v = [[]for i in range(K)]
    if (K == 0 or K > N):
        print("Not Possible", end="")
    else:
        print("The Subset Combinations are: ")
        PartitionSub(arr, 0, N, K, 0, v)


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    K = 2
    N = len(arr)
    partKSubsets(arr, N, K)
