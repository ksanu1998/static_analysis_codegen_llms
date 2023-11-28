def countReduce(str):
    count = 0
    for i in range(len(str)):
        if str[i]!= str[-i-1]:
            count += 1
    return count
