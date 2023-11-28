#include <bits/stdc++.h> 
 #define int  long long int 
 using namespace std ;
 void solve ( int arr [ ] , int n ) {
// Create a hash map to store the count of each element
    unordered_map<int, int> count;
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    // Iterate through the array and check for each element if there is a pair
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                count[arr[i]]--;
                if (count[arr[i]] == 0) {
                    count.erase(arr[i]);
                }
                break;
            }
        }
    }

    // Print the count of each distinct pair
    for (auto it = count.begin(); it!= count.end(); it++) {
        cout << it->first << " " << it->second << endl;
    }
}

int main() {
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    solve(arr, n);
    return 0;
}