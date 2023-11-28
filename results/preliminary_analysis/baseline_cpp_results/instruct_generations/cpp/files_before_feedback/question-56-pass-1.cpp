#include <bits/stdc++.h> 
 using namespace std ;
float productOfGP ( float a, float r, int n ) {
    float product = 1;
    for ( int i = 0 ; i < n ; i++ ) {
        product *= ( a * ( 1 - r ) );
        a *= r;
    }
    return product;
}