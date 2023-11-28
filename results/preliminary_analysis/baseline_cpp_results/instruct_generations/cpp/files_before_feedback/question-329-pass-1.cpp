#include <bits/stdc++.h> 
 using namespace std ;
 void findMax ( int a [ ] , int n ) {
int max = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > max) {
            max = a[i];
        }
    }
    cout << "Maximum value in the array is: " << max << endl;
}