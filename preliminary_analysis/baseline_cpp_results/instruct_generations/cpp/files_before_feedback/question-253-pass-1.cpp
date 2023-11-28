#include <bits/stdc++.h> 
 using namespace std ;
int getHermiteNumber(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= 2 * i;
    }
    return result;
}