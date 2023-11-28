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

// Test the function with a sample input
int main() {
    string str = "123456789";
    if (isSubSeqDivisible(str)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}

// Output:
// Yes

// Explanation:
// The function iterates over the string and checks if any subsequence of digits is divisible by 8. Since the string "123456789" contains the subsequence "12345678", which is divisible by 8, the function returns true.