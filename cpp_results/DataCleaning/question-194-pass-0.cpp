// Find the number of divisors of all numbers in the range [ 1 , n ]. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void findDivisors ( int n ) {
 
    // Create an array to store the divisors of n.
    int divisors[n+1];
    memset ( divisors, 0, sizeof divisors );
 
    // Initialize the divisors array.
    for ( int i = 1 ; i <= n ; i++ ) {
        for ( int j = i ; j <= n ; j += i )
            divisors[j]++;
    }
 
    // Print the divisors of n.
    for ( int i = 1 ; i <= n ; i++ )
        cout << divisors[i] << " ";
}
 
// Driver program to test above function.
int main () {
    int n = 10;
    findDivisors ( n );
    return 0;
}






















































































































































































































































































