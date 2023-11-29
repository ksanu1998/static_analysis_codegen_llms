#include <bits/stdc++.h> 
 using namespace std ;
int xorK(int n, int k) {
    int result = n;
    for (int i = 0; i < k; i++) {
        result = result ^ n;
    }
    return result;
}