#include <bits/stdc++.h> 
 using namespace std ;
int countSquares(int row, int column) {
    // Initialize the count to 1, as the bishop can visit its own square
    int count = 1;

    // Check if the bishop can visit any other squares in the same row
    for (int i = 0; i < column; i++) {
        if (row == i) {
            count++;
        }
    }

    // Check if the bishop can visit any other squares in the same column
    for (int i = 0; i < row; i++) {
        if (column == i) {
            count++;
        }
    }

    // Return the count of squares that can be visited by the bishop
    return count;
}