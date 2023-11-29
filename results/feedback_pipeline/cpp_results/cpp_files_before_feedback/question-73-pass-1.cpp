#include <bits/stdc++.h> 
 using namespace std ;
bool isoctagonal(int N) {
    int n = (int)sqrt(24*N+1);
    return (n*(n-1)) == 8*N;
}