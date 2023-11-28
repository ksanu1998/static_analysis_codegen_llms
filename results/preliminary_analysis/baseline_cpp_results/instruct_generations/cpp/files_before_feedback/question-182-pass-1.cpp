#include <iostream> 
 using namespace std ;
bool isEven(int arr[], int n, int r) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum % r == 0;
}