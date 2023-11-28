#include <bits/stdc++.h> 
 using namespace std ;
 void findAandB ( double N ) {
// Find the square root of N
    double sqrtN = sqrt(N);

    // Check if the square root is an integer
    if (sqrtN == (int)sqrtN) {
        // If the square root is an integer, then the number is a perfect square
        double a = sqrtN;
        double b = N / a;
        cout << "a = " << a << ", b = " << b << endl;
    } else {
        // If the square root is not an integer, then the number is not a perfect square
        // Find the two numbers that sum to N and have a product of N
        for (int i = 1; i <= N; i++) {
            for (int j = i; j <= N; j++) {
                if (i + j == N && i * j == N) {
                    cout << "a = " << i << ", b = " << j << endl;
                    break;
                }
            }
        }
    }
}

int main() {
    double N;
    cout << "Enter a number: ";
    cin >> N;
    findAandB(N);
    return 0;
}