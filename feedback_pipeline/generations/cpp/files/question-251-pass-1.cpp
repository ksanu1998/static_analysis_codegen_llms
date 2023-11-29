#include <bits/stdc++.h> 
 using namespace std ;
int minimumX(int n, int k) {
    int x = 1;
    while (x % k!= n) {
        x++;
    }
    return x;
}