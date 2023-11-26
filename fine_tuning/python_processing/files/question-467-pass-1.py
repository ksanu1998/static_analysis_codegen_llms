def countFreq(pat, txt):
    count = 0
    for i in range(len(txt)):
        if txt[i:i+len(pat)] == pat:
            count += 1
    return count
