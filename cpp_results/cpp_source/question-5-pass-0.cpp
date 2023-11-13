// Count of quadruples with product of a pair equal to the product of the remaining pair. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void sameProductQuadruples ( int nums [ ] , int N ) {
 
    int i, j, k, l ;
    int product ;
    int count = 0 ;
    for ( i = 0 ; i < N ; i++ ) {
        for ( j = i + 1 ; j < N ; j++ ) {
            for ( k = j + 1 ; k < N ; k++ ) {
                for ( l = k + 1 ; l < N ; l++ ) {
                    product = nums [ i ] * nums [ j ] * nums [ k ] * nums [ l ] ;
                    if ( product == nums [ i ] * nums [ j ] * nums [ k ] ) {
                        count++ ;
                    }
                }
            }
        }
    }
    cout << "Count of quadruples with product of a pair equal to the product of the remaining pair is : " << count << endl ;
 }
 int main ( ) {
    int nums [ ] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 } 