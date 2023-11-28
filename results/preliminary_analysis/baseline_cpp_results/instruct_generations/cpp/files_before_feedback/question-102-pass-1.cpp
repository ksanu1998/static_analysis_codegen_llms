#include <bits/stdc++.h> 
 using namespace std ;
 void movesRequired ( int a , int b ) {
// Initialize the result variable
    int result = 0;

    // While a is not divisible by b
    while (a % b!= 0) {
        // Decrement a by 1
        a--;
        // Increment the result by 1
        result++;
    }

    // Return the result
    return result;
}

int main() {
    // Test case 1: 12 and 3
    cout << movesRequired(12, 3) << endl; // Output: 2

    // Test case 2: 10 and 5
    cout << movesRequired(10, 5) << endl; // Output: 1

    // Test case 3: 15 and 5
    cout << movesRequired(15, 5) << endl; // Output: 3

    return 0;
}