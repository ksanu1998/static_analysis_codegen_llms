// Find the number of squares inside the given square grid. 
 #include <iostream> 
 using namespace std ;
 int cnt_squares ( int n ) {
 
     int cnt = 0 ;
     for ( int i = 1 ; i <= n ; i++ ) {
         for ( int j = 1 ; j <= n ; j++ ) {
             if ( i == j || i + j == n + 1 )
                 cnt++ ;
         }
     }
     return cnt ;
 }
 
 int main ( ) {
     int n ;
     cin >> n ;
     cout << cnt_squares ( n ) << endl ;
     return 0 ;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
