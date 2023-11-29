#include <algorithm>
#include <iostream>
using namespace std;
void CreateArray(int N, int even, int odd) {
    int* arr = new int[N];
    int i = 0;
    while (i < N) {
        if (i % 2 == 0) {
            arr[i] = even;
        } else {
            arr[i] = odd;
        }
        i++;
    }
    return arr;
}