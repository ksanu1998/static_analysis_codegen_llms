#include <bits/stdc++.h> 
 using namespace std ;
int max_sum(int a[], int n) {
    int max_val = a[0], sum = a[0];
    for (int i = 1; i < n; i++) {
        sum = max(sum + a[i], a[i]);
        max_val = max(max_val, sum);
    }
    return max_val;
}