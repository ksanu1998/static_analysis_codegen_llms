#include <bits/stdc++.h>
using namespace std;
void findNumbers(int n) {
    // Initialize an array to store the numbers
    int numbers[n];
    // Initialize the sum to 0
    int sum = 0;
    // Loop through each number from 1 to n
    for (int i = 1; i <= n; i++) {
        // If the sum is a perfect square, add the number to the array
        if (sum * sum == i) {
            numbers[i - 1] = i;
        }
        // Increment the sum by the current number
        sum += i;
    }
    // Print the array
    for (int i = 0; i < n; i++) {
        cout << numbers[i] << " ";
    }
    cout << endl;
}
int main() {
    int n;
    cin >> n;
    findNumbers(n);
    return 0;
}