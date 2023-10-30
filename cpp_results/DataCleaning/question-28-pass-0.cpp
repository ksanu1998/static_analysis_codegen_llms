// Find two numbers with given sum and maximum possible LCM. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void maxLCMWithGivenSum ( int X ) {
 
    int n = sqrt ( X ) ;
    for ( int i = 1 ; i <= n ; i++ ) {
        int j = X / i ;
        if ( j > i ) {
            int lcm = ( i * j ) ;
            if ( lcm % 2 == 0 ) {
                cout << "LCM of " << i << " and " << j << " is " << lcm << endl ;
                return ;
            }
        }
    }
    cout << "No such pair exists" << endl ;
}
 
int main ( ) {
    int X ;
    cout << "Enter the sum : " ;
    cin >> X ;
    maxLCMWithGivenSum ( X ) ;
    return 0 ;
}




























































































































































































































































































