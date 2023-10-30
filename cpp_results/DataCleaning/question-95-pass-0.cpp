// Nth positive number whose absolute difference of adjacent digits is at most 1. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void findNthNumber ( int N ) {
 
     int n = 1 ;
     int count = 0 ;
     while ( count < N ) {
         n = n * 10 + 1 ;
         int temp = n ;
         int count1 = 0 ;
         while ( temp > 0 ) {
             int digit = temp % 10 ;
             temp = temp / 10 ;
             if ( abs ( digit - temp % 10 ) <= 1 )
                 count1++ ;
         }
         if ( count1 == 10 )
             count++ ;
     }
     cout << n << endl ;
 }
 
 int main ( ) {
     int N ;
     cin >> N ;
     findNthNumber ( N ) ;
     return 0 ;
 }
