// Find the value of P and modular inverse of Q modulo 998244353. 
 #include <bits/stdc++.h> 
 using namespace std ;
 long long calculate ( long long p , long long q ) {
 
     long long phi = ( p - 1 ) * ( q - 1 ) ;
     long long x = 1 ;
     long long y = 0 ;
     long long gcd = 1 ;
     long long temp = 0 ;
     while ( phi!= 0 ) {
         temp = phi ;
         phi = p % q ;
         x = y ;
         y = x - ( p / q ) * y ;
         gcd = temp ;
     }
     return gcd ;
 }
 
 int main ( ) {
     long long p = 998244353 ;
     long long q = 998244353 ;
     long long gcd = calculate ( p, q ) ;
     cout << "Modular Inverse of " << q << " modulo " << p << " is " << ( ( q * gcd ) % p ) << endl ;
     return 0 ;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
