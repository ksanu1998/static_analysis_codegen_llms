from math import ceil, log
maxsize = 100005
xor_tree = [0] * maxsize


def construct_Xor_Tree_Util(current, start, end, x):
    if start > end:
        return
    mid = (start + end) // 2
    xor_tree[current] = x ^ xor_tree[mid]
    construct_Xor_Tree_Util(current * 2, start, mid - 1, xor_tree[mid])
    construct_Xor_Tree_Util(current * 2 + 1, mid + 1, end, x)
