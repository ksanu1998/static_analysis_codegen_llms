// Construct longest possible sequence of unique elements with given LCM. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void constructArrayWithGivenLCM ( int N ) {
 
     int lcm = 1;
     for ( int i = 1; i < N; i++ ) {
         lcm = lcm * i / __gcd ( lcm, i );
     }
 
     int count = 0;
     int j = 1;
     while ( count < N ) {
         if ( lcm % j == 0 ) {
             cout << j << " ";
             count++;
         }
         j++;
     }
 }
 
 int main () {
     int N;
     cin >> N;
     constructArrayWithGivenLCM ( N );
     return 0;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 