dim = 3


class Node:
    def __init__(self, data):
        self .data = data
        self .prev = None
        self .up = None
        self .down = None
        self .next = None


def createNode(data):
    temp = Node(data)
    return temp


def constructDoublyListUtil(mtrx, i, j, curr):
    if (i >= dim or j >= dim):
        return None
    temp = createNode(mtrx[i][j])
    temp .prev = curr
    temp .up = curr
    temp .next = constructDoublyListUtil(mtrx, i, j + 1, temp)
    temp .down = constructDoublyListUtil(mtrx, i + 1, j, temp)
    return temp


def constructDoublyList(mtrx):
    return constructDoublyListUtil(mtrx, 0, 0, None)


def display(head):
    rPtr = None
    dPtr = head
    while (dPtr is not None):
        rPtr = dPtr
        while (rPtr is not None):
            print(rPtr .data, end=' ')
            rPtr = rPtr .next
        print()
        dPtr = dPtr .down


if __name__ == "__main__":
    mtrx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list = constructDoublyList(mtrx)
    display(list)
