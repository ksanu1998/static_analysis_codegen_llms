#include <bits/stdc++.h> 
 using namespace std ;
bool sumOfTwoCubes(int n) {
    int x = (int)sqrt(n);
    if (x * x * x == n) return true;
    for (int i = x + 1; i <= n; i++) {
        int y = n - i * i;
        if (y * y * y == i * i) return true;
    }
    return false;
}