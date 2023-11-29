#include <bits/stdc++.h> 
 using namespace std ;
bool isPossible(int n, int k, int arr[]) {
    // Initialize a hash map to store the count of each element
    unordered_map<int, int> count;
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    // Iterate through the hash map and check if any element is not possible to make equal
    for (auto it = count.begin(); it!= count.end(); it++) {
        int key = it->first;
        int value = it->second;
        if (value % k!= 0) {
            return false;
        }
    }

    return true;
}