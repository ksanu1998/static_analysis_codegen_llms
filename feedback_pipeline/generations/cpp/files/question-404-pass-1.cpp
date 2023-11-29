#include <bits/stdc++.h> 
 using namespace std ;
 bool isSubSeqDivisible ( string str ) {
// Initialize variables
    int n = str.length();
    int count = 0;

    // Iterate over the string
    for (int i = 0; i < n; i++) {
        // Check if the current digit is divisible by 8
        if (str[i] % 8 == 0) {
            // Increment the count if the digit is divisible by 8
            count++;
        }
    }

    // Return true if the count is greater than 0, otherwise return false
    return count > 0;
}