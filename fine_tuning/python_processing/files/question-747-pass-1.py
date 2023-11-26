def build_tree(b, seg_tree, l, r, vertex):
    if l == r:
        seg_tree[vertex] = b[l]
        return seg_tree[vertex]
    
    mid = (l + r) // 2
    seg_tree[vertex] = max(build_tree(b, seg_tree, l, mid, vertex*2), build_tree(b, seg_tree, mid+1, r, vertex*2+1))
    return seg_tree[vertex]
