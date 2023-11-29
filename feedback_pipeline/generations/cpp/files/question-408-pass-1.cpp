#include <bits/stdc++.h> 
 using namespace std ;
 int smallestSumSubarr ( int arr [ ] , int n ) {
int min_sum = INT_MAX;
int curr_sum = 0;
for ( int i = 0 ; i < n ; i++ ) {
curr_sum += arr[i];
if ( curr_sum < min_sum ) {
min_sum = curr_sum;
}
if ( curr_sum > 0 ) {
curr_sum = 0;
}
}
return min_sum;
}