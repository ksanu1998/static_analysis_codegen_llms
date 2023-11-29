#include <bits/stdc++.h> 
 using namespace std ;
int maxCost(int a[], int n, int l, int r) {
    if (l > r) return 0;
    int m = (l + r) / 2;
    int cost1 = maxCost(a, n, l, m);
    int cost2 = maxCost(a, n, m + 1, r);
    int cost3 = 0;
    for (int i = m; i >= l; i--) {
        cost3 = max(cost3, cost1 + a[i]);
    }
    for (int i = m + 1; i <= r; i++) {
        cost3 = max(cost3, cost2 + a[i]);
    }
    return cost3;
}