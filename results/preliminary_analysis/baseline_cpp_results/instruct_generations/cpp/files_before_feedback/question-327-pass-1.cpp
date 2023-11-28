#include <iostream> 
 using namespace std ;
int maxLengthSquare(int row, int column, int arr[][4], int k) {
    int maxLength = 0;
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < column; j++) {
            int sum = 0;
            for (int m = i; m < row; m++) {
                for (int n = j; n < column; n++) {
                    sum += arr[m][n];
                    if (sum == k) {
                        maxLength = max(maxLength, m - i + 1);
                    }
                }
            }
        }
    }
    return maxLength;
}