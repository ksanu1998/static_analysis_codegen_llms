#include <bits/stdc++.h>
using namespace std;
int largestNumberLessThanOrEqualToZThatLeavesRemainderXWhenDividedByY(int x, int y, int z) {
    // Calculate the largest number less than or equal to z that leaves a remainder x when divided by y
    return (z / y) * y + x;
}