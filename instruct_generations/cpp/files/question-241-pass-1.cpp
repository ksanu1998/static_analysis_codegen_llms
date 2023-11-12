#include <bits/stdc++.h> 
 using namespace std ;
int smallestMultiple(int a[3]) {
    int n = 1;
    for (int i = 0; i < 3; i++) {
        n *= a[i];
    }
    return n;
}