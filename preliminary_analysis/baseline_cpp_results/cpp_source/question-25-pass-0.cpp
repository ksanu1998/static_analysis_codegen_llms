// Find temperature of missing days using given sum and average. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void findTemperature ( int x , int y , int s ) {
 
     int avg = s / x ;
     int rem = s % x ;
     int i = 0 ;
     while ( i < x ) {
         if ( i < rem ) {
             cout << avg + 1 << " " ;
             i++ ;
         }
         else {
             cout << avg << " " ;
             i++ ;
         }
     }
 }
 int main ( ) {
     int x, y, s ;
     cin >> x >> y >> s ;
     findTemperature ( x, y, s ) ;
     return 0 ;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 