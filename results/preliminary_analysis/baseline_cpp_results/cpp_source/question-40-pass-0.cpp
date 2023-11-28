// Sum of sum. 
 #include <bits/stdc++.h> 
 using namespace std ;
 static long sumOfSumSeries ( int N ) {
 
    long sum = 0 ;
    for ( int i = 1 ; i <= N ; i++ ) {
        sum += i ;
    }
    return sum ;
 }
 
 static long sumOfSquareSeries ( int N ) {
 
    long sum = 0 ;
    for ( int i = 1 ; i <= N ; i++ ) {
        sum += i * i ;
    }
    return sum ;
 }
 
 static long sumOfCubeSeries ( int N ) {
 
    long sum = 0 ;
    for ( int i = 1 ; i <= N ; i++ ) {
        sum += i * i * i ;
    }
    return sum ;
 }
 
 static long sumOfFourthPowerSeries ( int N ) {
 
    long sum = 0 ;
    for ( int i = 1 ; i <= N ; i++ ) {
        sum += i * i * i * i ;
    }
    return sum ;
 }
 
 static long sumOfFifthPowerSeries ( int N ) {
 
    long sum = 0 ;
    for ( int i = 1 ; i <= N ; i++ ) {
        sum += i * i * i * i * i ;
    }
    return sum ;
 }
 
 static long sumOfSixthPowerSeries ( int N ) {
 
    long sum = 0 ;
    for ( int i = 1 ; i <= N ; i++ ) {
        sum += i * i * i * i * i * i ;
    }
    return sum ;
 }
 
 static long sumOfSeventhPowerSeries ( int N ) {
 
    long sum = 0 ;
    for ( int i = 1 ; i <= N ; i++ ) {
        sum += i * i * i * i * i * i * i ;
    }
    return sum ;
 }
 
 static long sumOfEighthPowerSeries ( int N ) {
 
    long sum = 0 ;
   