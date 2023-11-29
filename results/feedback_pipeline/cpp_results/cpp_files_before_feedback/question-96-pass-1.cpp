#include <bits/stdc++.h> 
 using namespace std ;
 int findUniqueElements ( int arr [ ] , int N , int K ) {
// Create a hash map to store the frequency of each element
    unordered_map<int, int> freq;
    for (int i = 0; i < N; i++) {
        freq[arr[i]]++;
    }
    // Find the element that occurs once
    for (int i = 0; i < N; i++) {
        if (freq[arr[i]] == 1) {
            return arr[i];
        }
    }
    return -1;
}