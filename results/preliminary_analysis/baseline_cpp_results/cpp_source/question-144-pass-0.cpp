// Find X and Y intercepts of a line passing through the given points. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void getXandYintercept ( int P [ ] , int Q [ ] ) {
 
    int x1 = P [ 0 ] ;
    int y1 = P [ 1 ] ;
    int x2 = Q [ 0 ] ;
    int y2 = Q [ 1 ] ;
    int x3 = P [ 2 ] ;
    int y3 = P [ 3 ] ;
    int x4 = Q [ 2 ] ;
    int y4 = Q [ 3 ] ;
    int a = ( y1 - y2 ) ;
    int b = ( x2 - x1 ) ;
    int c = ( x1 * y2 - x2 * y1 ) ;
    int d = ( y3 - y4 ) ;
    int e = ( x4 - x3 ) ;
    int f = ( x3 * y4 - x4 * y3 ) ;
    int x = ( e * c - b * f ) / ( a * e - b * d ) ;
    int y = ( a * f - b * c ) / ( a * e - b * d ) ;
    cout << "X intercept of the line passing through the given points is " << x << " and Y intercept is " << y << endl ;
 }
 int main ( ) {
    int P [ ] = { 1, 2, 3, 4 } 