#include <bits/stdc++.h> 
 using namespace std ;
int countWays(int n, int l, int r) {
    int count = 0;
    for (int i = l; i <= r; i++) {
        if (i % 2 == 0) {
            count++;
        }
    }
    return count;
}