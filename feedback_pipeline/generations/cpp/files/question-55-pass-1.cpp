#include <bits/stdc++.h> 
 using namespace std ;
 
bool isCenteredcube ( int N ) {
    int x = sqrt ( N );
    return ( x * x * x == N );
}