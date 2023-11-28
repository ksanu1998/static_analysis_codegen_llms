// Find sum of inverse of the divisors when sum of divisors and the number is given. 
 #include <bits/stdc++.h> 
 using namespace std ;
 double SumofInverseDivisors ( int N , int Sum ) {
 
    // Initialize the sum of inverse of divisors as 0.
    double SumofInverseDivisors = 0 ;
 
    // Initialize the sum of divisors as 0.
    int SumofDivisors = 0 ;
 
    // Initialize the number of divisors as 0.
    int NumberofDivisors = 0 ;
 
    // Traverse from 1 to N.
    for ( int i = 1 ; i <= N ; i++ ) {
 
        // If i divides N, then count it as divisor.
        if ( N % i == 0 ) {
 
            // Increase the number of divisors.
            NumberofDivisors++ ;
 
            // Add the divisor to the sum of divisors.
            SumofDivisors += i ;
        }
    }
 
    // If the sum of divisors is equal to the given sum, then
    // return the sum of inverse of divisors.
    if ( SumofDivisors == Sum ) {
        for ( int i = 1 ; i <= N ; i++ ) {
 
            // If i divides N, then count it as divisor.
            if ( N % i == 0 ) {
 
                // Add the inverse of divisor to the sum of inverse of divisors.
                SumofInverseDivisors += 1 / ( double ) i ;
            }
        }
 
        // Return the sum of inverse of divisors.
        return SumofInverseDivisors ;
    }
 
    // If the sum of divisors is not equal to the given sum, then
    // return -1.
    return -1 ;
}
 
// Driver program to test above function.
int main () {
 
    // Number of test cases.
    int T ;
    cin >> T ;
 
    // Loop for test cases.
    while ( T-- ) {
