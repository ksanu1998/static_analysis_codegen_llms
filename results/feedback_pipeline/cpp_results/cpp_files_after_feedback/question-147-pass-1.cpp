#include <bits/stdc++.h>
using namespace std;
void find_numbers(int N) {
    // Initialize an array to store the three numbers
    int numbers[3];
    // Initialize the sum to 0
    int sum = 0;
    // Loop through the numbers from 1 to N
    for (int i = 1; i <= N; i++) {
        // If the number is not already in the array
        if (numbers[0]!= i && numbers[1]!= i && numbers[2]!= i) {
            // Add the number to the array
            numbers[sum++] = i;
            // If the sum is equal to 2, we have found the three numbers
            if (sum == 3) {
                break;
            }
        }
    }
    // Print the three numbers
    for (int i = 0; i < sum; i++) {
        cout << numbers[i] << " ";
    }
    // End the program
    return 0;
}