#include <iostream>
using namespace std;
#define row 5
#define col 5
bool isPath(int arr[row][col]) {
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (arr[i][j] == 1) {
                return true;
            }
        }
    }
    return false;
}
int main() {
    int arr[row][col] = {
        {1, 0, 0, 0, 0},
        {0, 1, 0, 0, 0},
        {0, 0, 1, 0, 0},
        {0, 0, 0, 1, 0},
        {0, 0, 0, 0, 1}
    };
    if (isPath(arr)) {
        cout << "There is a path in the matrix." << endl;
    } else {
        cout << "There is no path in the matrix." << endl;
    }
    return 0;
}