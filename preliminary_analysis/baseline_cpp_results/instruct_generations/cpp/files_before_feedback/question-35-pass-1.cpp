#include <bits/stdc++.h> 
 using namespace std ;
 int prefixProduct ( int a [ ] , int n ) {
int prefixProduct[n+1];
prefixProduct[0] = 1;
for (int i = 1; i <= n; i++) {
    prefixProduct[i] = prefixProduct[i-1] * a[i-1];
}
return prefixProduct[n];
}