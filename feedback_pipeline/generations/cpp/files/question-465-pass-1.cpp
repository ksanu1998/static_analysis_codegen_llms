#include <bits/stdc++.h> 
 using namespace std ;
int nthTerm(int N) {
    if (N == 1) {
        return 4;
    } else if (N % 2 == 0) {
        return 2;
    } else {
        return 3;
    }
}