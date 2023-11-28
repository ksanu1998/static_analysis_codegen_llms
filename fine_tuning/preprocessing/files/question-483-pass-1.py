def rearrangeString(s1, s2):
    # Check if s2 is a subsequence of s1
    if s2 in s1:
        # Find the index of the first occurrence of s2 in s1
        index = s1.find(s2)
        # If the index is not -1, remove the subsequence from s1
        if index!= -1:
            s1 = s1[:index] + s1[index+len(s2):]
    return s1
