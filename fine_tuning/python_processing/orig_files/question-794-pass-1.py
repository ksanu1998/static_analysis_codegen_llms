def nextGreaterInLeft(a):
    left_index = [0] * len(a)
    s = []
    for i in range(len(a)):
        while len(s) != 0 and a[i] >= a[s[-1]]:
            s .pop()
        if len(s) != 0:
            left_index[i] = s[-1]
        else:
            left_index[i] = 0
        s .append(i)
    return left_index


def nextGreaterInRight(a):
    right_index = [0] * len(a)
    s = []
    for i in range(len(a) - 1, -1, -1):
        while len(s) != 0 and a[i] >= a[s[-1]]:
            s .pop()
        if len(s) != 0:
            right_index[i] = s[-1]
        else:
            right_index[i] = 0
        s .append(i)
    return right_index


def LRProduct(arr):
    left = nextGreaterInLeft(arr)
    right = nextGreaterInRight(arr)
    ans = -1
    for i in range(1, len(left) - 1):
        if left[i] == 0 or right[i] == 0:
            ans = max(ans, 0)
        else:
            temp = (left[i] + 1) * (right[i] + 1)
            ans = max(ans, temp)
    return ans


arr = [5, 4, 3, 4, 5]
print(LRProduct(arr))
