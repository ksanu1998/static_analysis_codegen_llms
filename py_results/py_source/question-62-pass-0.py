# Count of nodes having odd divisors in the given subtree for Q queries. 
import math
N = 100001
adj = [[]for i in range(N)]
a = [0 for i in range(N)]
ans = [0 for i in range(N)]


def hasOddNumberOfDivisors(n): 
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1): 
        if n % i == 0: 
            count += 2
    if n!= 1 and count % 2 == 0: 
        count += 1
    return count 

def dfs(u, par): 
    for v in adj[u]: 
        if v!= par: 
            dfs(v, u) 
            ans[u] += ans[v] 
            ans[u] += hasOddNumberOfDivisors(a[v]) 


def solve(): 
    n, q = map(int, input().split())
    for i in range(n - 1): 
        u, v = map(int, input().split())
        adj[u].append(v) 
        adj[v].append(u) 
    for i in range(n): 
        a[i] = int(input()) 
    dfs(0, -1) 
    for i in range(q): 
        u, v = map(int, input().split())
        print(ans[u] - ans[v]) 


solve()








































































































































