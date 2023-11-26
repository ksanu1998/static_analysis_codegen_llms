def minFlips(target):
    count = 0
    for i in range(len(target)):
        if target[i] == "0":
            count += 1
            target = target[:i] + "1" + target[i+1:]
    return count
