// Find the conjugate of a Complex number. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void solve ( string s ) {
 
    int n = s.length() ;
    int i = 0 ;
    int j = n-1 ;
    while ( i < j ) {
        swap ( s[i], s[j] ) ;
        i++ ;
        j-- ;
    }
    cout << s << endl ;
 }
 int main ( ) {
    string s = "1+2i" ;
    solve ( s ) ;
    return 0 ;
 }












































































































































































































































































































































































