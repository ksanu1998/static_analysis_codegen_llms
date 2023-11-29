#include <bits/stdc++.h> 
 using namespace std ;
 const int MAX = 40 ;
 int dp [ MAX ] [ 9 * MAX + 1 ] ;
int countGroups(int position, int previous_sum, int length, char *num) {
    if (position == length) {
        return 1;
    }
    if (dp[position][previous_sum]!= -1) {
        return dp[position][previous_sum];
    }
    int count = 0;
    for (int i = 0; i < 9; i++) {
        if (previous_sum + i * pow(10, length - position - 1) <= MAX) {
            count += countGroups(position + 1, previous_sum + i * pow(10, length - position - 1), length, num);
        }
    }
    return dp[position][previous_sum] = count;
}