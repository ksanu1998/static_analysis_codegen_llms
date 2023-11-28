def MaxPrefix(string):
    Dict = {}
    maxprefix = 0
    for i in string:
        Dict[i] = Dict .get(i, 0) + 1
    minfrequency = min(Dict .values())
    countminFrequency = 0
    for x in Dict:
        if (Dict[x] == minfrequency):
            countminFrequency += 1
    mapper = {}
    indi = 0
    for i in string:
        mapper[i] = mapper .get(i, 0) + 1
        if (mapper[i] > countminFrequency):
            break
        indi += 1
    print(string[:indi])


if __name__ == '__main__':
    str = 'aabcdaab'
    MaxPrefix(str)
