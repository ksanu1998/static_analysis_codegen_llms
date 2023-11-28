// Sum of sum. 
 #include <iostream> 
 #include <math.h> 
 using namespace std ;
 long sumOfSumSeries ( int n ) {
 
    long sum = 0 ;
    for ( int i = 1 ; i <= n ; i++ ) {
        sum += i ;
    }
    return sum ;
 }
 
 long sumOfSquareSeries ( int n ) {
 
    long sum = 0 ;
    for ( int i = 1 ; i <= n ; i++ ) {
        sum += pow ( i, 2 ) ;
    }
    return sum ;
 }
 
 long differenceOfSquareSeriesAndSumOfSumSeries ( int n ) {
 
    long sumOfSumSeries = sumOfSumSeries ( n ) ;
    long sumOfSquareSeries = sumOfSquareSeries ( n ) ;
    return sumOfSquareSeries - sumOfSumSeries ;
 }
 
 int main ( ) {
 
    int n ;
    cout << "Enter the value of n : " ;
    cin >> n ;
    cout << "The difference of square series and sum of sum series is : " << differenceOfSquareSeriesAndSumOfSumSeries ( n ) ;
    return 0 ;
 }



























































































































































































































