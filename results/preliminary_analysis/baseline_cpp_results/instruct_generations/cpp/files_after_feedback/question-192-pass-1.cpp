#include <bits/stdc++.h>
using namespace std;
void printPosition(const int A[], const int B[], int sizeOfA, int sizeOfB) {
    // Initialize variables
    int i = 0;
    int j = 0;
    // Loop through the arrays
    while (i < sizeOfA && j < sizeOfB) {
        // Check if the current element of A is equal to the current element of B
        if (A[i] == B[j]) {
            // If they are equal, print the position of the element
            cout << "The position of the element " << B[j] << " in the array A is " << i << endl;
            j++;
        } else {
            // If they are not equal, increment the index of A
            i++;
        }
    }
}
int main() {
    // Initialize arrays
    int A[] = {1, 2, 3, 4, 5};
    int B[] = {2, 3, 4};
    // Find the position of the elements in B in A
    printPosition(A, B, 5, 3);
    return 0;
}