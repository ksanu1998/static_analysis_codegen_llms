#include <bits/stdc++.h> 
 using namespace std ;
int nthTerm(int N) {
    if (N == 1) {
        return 2;
    } else if (N == 2) {
        return 3;
    } else {
        return nthTerm(N - 1) + nthTerm(N - 2);
    }
}