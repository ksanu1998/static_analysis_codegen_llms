#include <bits/stdc++.h> 
 using namespace std ;
 void candies ( int n , int k ) {
// Initialize an array to store the number of candies for each person
    int candies[k];
    // Fill the array with 0s
    fill(candies, candies + k, 0);
    // Distribute the candies
    for (int i = 0; i < n; i++) {
        // Find the person with the least number of candies
        int min_index = 0;
        for (int j = 1; j < k; j++) {
            if (candies[j] < candies[min_index]) {
                min_index = j;
            }
        }
        // Increment the number of candies for that person
        candies[min_index]++;
    }
    // Print the final distribution
    for (int i = 0; i < k; i++) {
        cout << candies[i] << " ";
    }
    cout << endl;
}

int main() {
    int n, k;
    cin >> n >> k;
    candies(n, k);
    return 0;
}