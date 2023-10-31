// Find the position of box which occupies the given ball. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void printPosition ( int A [ ] , int B [ ] , int sizeOfA , int sizeOfB ) {
 
     int i, j ;
     for ( i = 0 ; i < sizeOfA ; i++ ) {
         for ( j = 0 ; j < sizeOfB ; j++ ) {
             if ( A [ i ] == B [ j ] ) {
                 cout << "(" << i << "," << j << ")" << endl ;
                 break ;
             }
         }
     }
 }
 int main ( ) {
     int A [ ] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 } 