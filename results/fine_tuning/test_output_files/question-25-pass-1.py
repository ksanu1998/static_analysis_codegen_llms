def findTemperature(x, y, s):
    n = len(s)
    sum = 0
    for i in range(n):
        sum += s[i]
    if (sum < x):
        print("No missing days")
        return
    if (sum > x):
        print("More than one missing days")
        return
    if (sum == x):
        print("No missing days")
        return
    if (sum < 2 * x):
        print("One missing day")
        return
    if (sum > 2 * x):
        print("More than one missing days")
        return


if __name__ == "__main__":
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 15
    y = 5
    findTemperature(x, y, s)
