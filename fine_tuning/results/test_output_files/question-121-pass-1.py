def calNum(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0


if __name__ == "__main__":
    year = 1900
    year1 = 2000
    print(calNum(year1) - calNum(year))
