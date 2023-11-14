#include <bits/stdc++.h>
using namespace std;
void powerfulIntegers(int x, int y, int bound) {
    // Initialize a set to store the powerful integers
    set<int> powerfulIntegers;
    // Loop through all possible values of x
    for (int i = 0; i <= bound; i++) {
        // Calculate the power of 2 of x
        int powerOfX = pow(2, i);
        // Loop through all possible values of y
        for (int j = 0; j <= bound; j++) {
            // Calculate the power of 2 of y
            int powerOfY = pow(2, j);
            // Calculate the sum of the powers of 2 of x and y
            int sum = powerOfX + powerOfY;
            // Check if the sum is less than or equal to the bound
            if (sum <= bound) {
                // Add the sum to the set of powerful integers
                powerfulIntegers.insert(sum);
            }
        }
    }
    // Print the powerful integers
    for (auto powerfulInteger : powerfulIntegers) {
        cout << powerfulInteger << " ";
    }
    cout << endl;
}