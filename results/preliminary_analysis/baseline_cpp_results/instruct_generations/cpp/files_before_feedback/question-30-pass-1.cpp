#include <bits/stdc++.h> 
 using namespace std ;
int solve(int X, int Y) {
    int count = 0;
    while (X!= Y) {
        if (X > Y) {
            X = X - Y;
            count++;
        } else {
            Y = Y - X;
            count++;
        }
    }
    return count;
}