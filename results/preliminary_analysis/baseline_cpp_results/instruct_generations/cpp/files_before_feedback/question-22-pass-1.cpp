#include <bits/stdc++.h> 
 using namespace std ;
 void Kmultiples ( int n , int k ) {
// Initialize the result array
    int result[k];

    // Initialize the counter
    int i = 0;

    // Loop through the multiples of N
    while (i < k) {
        // Calculate the next multiple of N
        int multiple = n << i;

        // Store the result in the result array
        result[i] = multiple;

        // Increment the counter
        i++;
    }

    // Print the result array
    for (int i = 0; i < k; i++) {
        cout << result[i] << " ";
    }
    cout << endl;
}

int main() {
    int n = 2;
    int k = 5;
    Kmultiples(n, k);
    return 0;
}