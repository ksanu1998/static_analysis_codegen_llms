def permute(st, l, r, n):
    if l == r:
        print(st)
    else:
        for i in range(l, r+1):
            st.append(i)
            permute(st, i+1, r, n)
            st.pop()
