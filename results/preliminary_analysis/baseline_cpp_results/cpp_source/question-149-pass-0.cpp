// Minimum possible number with the given operation. 
 #include <bits/stdc++.h> 
 using namespace std ;
 string minInt ( string str ) {
 
    int n = str.length() ;
    int i = 0 ;
    while ( i < n && str[i] == '0' )
        i++ ;
    if ( i == n )
        return "0" ;
    return str.substr ( i, n - i ) ;
 }
 
 string maxInt ( string str ) {
 
    int n = str.length() ;
    int i = 0 ;
    while ( i < n && str[i] == '9' )
        i++ ;
    if ( i == n )
        return "9" ;
    return str.substr ( i, n - i ) ;
 }
 
 string minMaxInt ( string str ) {
 
    int n = str.length() ;
    int i = 0 ;
    while ( i < n && str[i] == '0' )
        i++ ;
    if ( i == n )
        return "0" ;
    string min = str.substr ( i, n - i ) ;
    int j = n - 1 ;
    while ( j >= 0 && str[j] == '9' )
        j-- ;
    if ( j < 0 )
        return "9" ;
    string max = str.substr ( j + 1, n - j - 1 ) ;
    return min + max ;
 }
 
 string minMaxInt2 ( string str ) {
 
    int n = str.length() ;
    int i = 0 ;
    while ( i < n && str[i] == '0' )
        i++ ;
    if ( i == n )
        return "0" ;
    string min = str.substr ( i, n - i ) ;
    int j = n - 1 ;
    while ( j >= 0 && str[j] == '9' )
        j-- ;
    if ( j < 0 )
        return "9" ;
    string max = str.substr ( j + 1, n - j