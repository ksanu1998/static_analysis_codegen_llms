#include <bits/stdc++.h> 
 using namespace std ;
 bool isTriPerfect ( int n ) {
int sum = 0 ;
for ( int i = 1 ; i <= n ; i++ ) {
sum += i ;
}
return sum == n ;