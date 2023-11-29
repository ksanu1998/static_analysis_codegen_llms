def Check_is_possible(l, r, k):
    if (l % k == 0 and r % k == 0):
        return 1
    if (l % k == 0 or r % k == 0):
        return 0
    if (l > r):
        return 0
    if (Check_is_possible(l, (l + r) / 2, k) == 1):
        return 1
    if (Check_is_possible((l + r) / 2, r, k) == 1):
        return 1
    return 0


if __name__ == "__main__":
    l = 1
    r = 10
    k = 3
    if (Check_is_possible(l, r, k) == 1):
        print("Yes")
    else:
        print("No")
