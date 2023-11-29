#include <bits/stdc++.h> 
 using namespace std ;
bool isPentadecagon(int N) {
    // Formula to check if a number is a Pentadecagonal Number:
    // (N * (3N - 1)) / 2
    int pentadecagonalNumber = (N * (3 * N - 1)) / 2;
    return pentadecagonalNumber == N;
}