#include <bits/stdc++.h> 
 using namespace std ;
int minMoves(long long n) {
    int moves = 0;
    while (n % 25!= 0) {
        n++;
        moves++;
    }
    return moves;
}