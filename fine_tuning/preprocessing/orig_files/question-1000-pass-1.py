from math import ceil, log
maxsize = 100005
xor_tree = [0] * maxsize


def construct_Xor_Tree_Util(current, start, end, x):
    if (start == end):
        xor_tree[x] = current[start]
        return
    left = x * 2 + 1
    right = x * 2 + 2
    mid = start + (end - start) // 2
    construct_Xor_Tree_Util(current, start, mid, left)
    construct_Xor_Tree_Util(current, mid + 1, end, right)
    xor_tree[x] = (xor_tree[left] ^ xor_tree[right])


def construct_Xor_Tree(arr, n):
    construct_Xor_Tree_Util(arr, 0, n - 1, 0)


if __name__ == '__main__':
    leaf_nodes = [40, 32, 12, 1, 4, 3, 2, 7]
    n = len(leaf_nodes)
    construct_Xor_Tree(leaf_nodes, n)
    x = (ceil(log(n, 2)))
    max_size = 2 * pow(2, x) - 1
    print("Nodes of the XOR Tree:")
    for i in range(max_size):
        print(xor_tree[i], end=" ")
    root = 0
    print("Root:", xor_tree[root])
