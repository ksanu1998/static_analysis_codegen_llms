#include <bits/stdc++.h> 
 using namespace std ;
 void constructArrayWithGivenLCM ( int N ) {
// Initialize an array to store the elements of the sequence
    int arr[N];

    // Initialize the first element of the sequence
    arr[0] = 1;

    // Loop through the remaining elements of the sequence
    for (int i = 1; i < N; i++) {
        // Find the least common multiple of the current element and the previous element
        int lcm = arr[i - 1] * i;

        // Add the least common multiple to the array
        arr[i] = lcm;
    }

    // Print the constructed sequence
    for (int i = 0; i < N; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int N;
    cin >> N;
    constructArrayWithGivenLCM(N);
    return 0;
}