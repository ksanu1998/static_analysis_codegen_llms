def Profit(costPrice, sellingPrice):
    profit = (sellingPrice - costPrice)
    return profit


def Loss(costPrice, sellingPrice):
    Loss = (costPrice - sellingPrice)
    return Loss


if __name__ == "__main__":
    costPrice, sellingPrice = 1500, 2000
    if sellingPrice == costPrice:
        print("No profit nor Loss")
    elif sellingPrice > costPrice:
        print(Profit(costPrice, sellingPrice), "Profit")
    else:
        print(Loss(costPrice, sellingPrice), "Loss")
