#include <bits/stdc++.h>
using namespace std;
const int NumUnsignBits = 64;
unsigned long findNum(unsigned long x) {
    unsigned long closest = 0;
    for (int i = 0; i < NumUnsignBits; i++) {
        closest |= (x & (1ul << i)) << (NumUnsignBits - i - 1);
    }
    return closest;
}