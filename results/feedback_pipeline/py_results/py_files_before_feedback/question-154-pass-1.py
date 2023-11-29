def minCost(arr, n):
    if n == 1:
        return 0
    min_cost = float('inf')
    for i in range(n):
        cost = abs(arr[i] - arr[i+1])
        min_cost = min(min_cost, cost)
    return min_cost