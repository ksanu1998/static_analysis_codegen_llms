#include <iostream>
using namespace std;
void printNumber(int holes) {
    // Initialize an array to store the numbers
    int numbers[holes];
    // Fill the array with numbers from 1 to holes
    for (int i = 0; i < holes; i++) {
        numbers[i] = i + 1;
    }
    // Print the numbers
    for (int i = 0; i < holes; i++) {
        cout << numbers[i] << " ";
    }
    cout << endl;
}
int main() {
    int holes;
    cout << "Enter the number of holes: ";
    cin >> holes;
    printNumber(holes);
    return 0;
}