#include <bits/stdc++.h> 
 using namespace std ;
int CountPairs(int arr[], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            count++;
        }
    }
    return count;
}