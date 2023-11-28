#include <bits/stdc++.h> 
 using namespace std ;
 void findMissingNums ( int even [ ] , int sizeEven , int odd [ ] , int sizeOdd ) {
// Find the missing even numbers
    int missingEvens[sizeEven];
    for (int i = 0; i < sizeEven; i++) {
        if (even[i] % 2 == 0) {
            missingEvens[i] = even[i];
        }
    }

    // Find the missing odd numbers
    int missingOdds[sizeOdd];
    for (int i = 0; i < sizeOdd; i++) {
        if (odd[i] % 2!= 0) {
            missingOdds[i] = odd[i];
        }
    }

    // Print the missing numbers
    cout << "Missing even numbers: ";
    for (int i = 0; i < sizeEven; i++) {
        if (missingEvens[i]!= 0) {
            cout << missingEvens[i] << " ";
        }
    }
    cout << endl;
    cout << "Missing odd numbers: ";
    for (int i = 0; i < sizeOdd; i++) {
        if (missingOdds[i]!= 0) {
            cout << missingOdds[i] << " ";
        }
    }
    cout << endl;
}

int main() {
    int even[] = {1, 2, 3, 4, 5, 6};
    int sizeEven = sizeof(even) / sizeof(even[0]);
    int odd[] = {1, 3, 5, 7, 9};
    int sizeOdd = sizeof(odd) / sizeof(odd[0]);
    findMissingNums(even, size