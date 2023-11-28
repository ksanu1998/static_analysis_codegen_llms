n = 7


def minheapify(a, index):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < len(a) and a[left] < a[smallest]:
        smallest = left
    if right < len(a) and a[right] < a[smallest]:
        smallest = right
    if smallest!= index:
        a[index], a[smallest] = a[smallest], a[index]
        minheapify(a, smallest)
