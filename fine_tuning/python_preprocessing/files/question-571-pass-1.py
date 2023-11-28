def maximum_one(s, n):
    max_length = 0
    for i in range(n):
        if s[i] == '1':
            current_length = 1
            for j in range(i+1, n):
                if s[j] == '1':
                    current_length += 1
                else:
                    break
            max_length = max(max_length, current_length)
    return max_length
