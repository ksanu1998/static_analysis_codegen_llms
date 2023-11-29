#include <bits/stdc++.h> 
 using namespace std ;
int maxResult(int n, int a, int b, int c) {
    int x, y, z;
    x = (n - a) / b;
    y = (n - a) / c;
    z = n / (a + b + c);
    return x + y + z;
}