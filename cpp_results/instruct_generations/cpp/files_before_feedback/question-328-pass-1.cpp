#include <bits/stdc++.h> 
 using namespace std ;
 const int N = 101 ;
 const int mod = 1e9 + 7 ;
 int exactsum [ N ] [ N ] [ N ] ;
 int exactnum [ N ] [ N ] [ N ] ;
int getSum(int x, int y, int z) {
    return exactsum[x][y][z] % mod;
}