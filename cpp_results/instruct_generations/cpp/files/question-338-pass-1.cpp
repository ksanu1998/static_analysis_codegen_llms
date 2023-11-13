#include <bits/stdc++.h> 
 using namespace std ;
int countWays(int n) {
    int ways = 1;
    for (int i = 1; i <= n; i++) {
        ways *= i;
    }
    return ways;
}