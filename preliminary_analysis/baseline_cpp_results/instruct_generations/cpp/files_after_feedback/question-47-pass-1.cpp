#include <iostream>
#include <math.h>
using namespace std;
int smallestNumber(int N) {
    int i = 1;
    while (i % N!= 0) {
        i++;
    }
    return i;
}
int main() {
    int N;
    cout << "Enter a positive integer: ";
    cin >> N;
    cout << "The smallest " << N << " digit number divisible by " << N << " is: " << smallestNumber(N) << endl;
    return 0;
}