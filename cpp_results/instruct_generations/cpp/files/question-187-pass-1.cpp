#include <bits/stdc++.h> 
 using namespace std ;
int changeTheArray(int arr[], int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            count++;
        }
    }
    return count;
}