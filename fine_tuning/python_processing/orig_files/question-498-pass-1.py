def check(s):
    a = set()
    for i in s:
        if i in a:
            return False
        a .add(i)
    return True


def helper(arr, ind):
    if (ind == len(arr)):
        return [""]
    tmp = helper(arr, ind + 1)
    ret = tmp
    for i in tmp:
        test = i + arr[ind]
        if (check(test)):
            ret .append(test)
    return ret


def maxLength(arr):
    tmp = helper(arr, 0)
    l = 0
    for i in tmp:
        l = l if l > len(i)else len(i)
    return l


if __name__ == '__main__':
    s = []
    s .append("abcdefgh")
    print(maxLength(s))
