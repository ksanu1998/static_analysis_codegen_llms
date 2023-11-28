#include <bits/stdc++.h> 
 using namespace std ;
 void PythagoreanTriplet ( int n ) {
// Initialize variables
    int a = 0, b = 0, c = 0;

    // Loop through all possible values of a
    for (int a = 1; a <= n; a++) {
        // Loop through all possible values of b
        for (int b = 1; b <= n; b++) {
            // Calculate the value of c
            int c = sqrt(a*a + b*b);

            // Check if c is an integer and if the sum of a, b, and c is equal to n
            if (c == (int)c && a + b + c == n) {
                // If the conditions are met, print the triplet
                cout << a << " " << b << " " << c << endl;
            }
        }
    }
}