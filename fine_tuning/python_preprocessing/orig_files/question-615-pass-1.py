from collections import defaultdict


def findWinner(votes):
    mapObj = defaultdict(int)
    for st in votes:
        mapObj[st] += 1
    maxValueInMap = 0
    winner = ""
    for entry in mapObj:
        key = entry
        val = mapObj[entry]
        if (val > maxValueInMap):
            maxValueInMap = val
            winner = key
        elif (val == maxValueInMap and winner > key):
            winner = key
    print(winner)


if __name__ == "__main__":
    votes = [
        "john",
        "johnny",
        "jackie",
        "johnny",
        "john",
        "jackie",
        "jamie",
        "jamie",
        "john",
        "johnny",
        "jamie",
        "johnny",
        "john"]
    findWinner(votes)
