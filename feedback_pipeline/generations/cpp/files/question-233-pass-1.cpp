#include <bits/stdc++.h> 
 using namespace std ;
int countPairs(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (((n % i) % j) % n == 0) {
                count++;
            }
        }
    }
    return count;
}