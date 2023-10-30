// Find maximum unreachable height using two ladders. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int maxHeight ( int h1 , int h2 ) {
 
     int max = 0 ;
     int min = 0 ;
     int max1 = 0 ;
     int min1 = 0 ;
     if ( h1 > h2 ) {
         max = h1 ;
         min = h2 ;
     }
     else {
         max = h2 ;
         min = h1 ;
     }
     if ( max % 2 == 0 ) {
         max1 = max / 2 ;
         min1 = min ;
     }
     else {
         max1 = max / 2 ;
         min1 = min + 1 ;
     }
     if ( max1 > min1 ) {
         return max1 ;
     }
     else {
         return min1 ;
     }
 }
 int main ( ) {
     int h1, h2 ;
     cin >> h1 >> h2 ;
     cout << maxHeight ( h1, h2 ) << endl ;
     return 0 ;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 