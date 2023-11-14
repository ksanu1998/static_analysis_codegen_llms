#include <bits/stdc++.h> 
 using namespace std ;
 void possibleToReach ( int x , int y , int z ) {
#include <bits/stdc++.h>
using namespace std;

void possibleToReach(int x, int y, int z) {
    if (x == y && y == 0) {
        if (z == 0) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
        return;
    }

    if (x > y) {
        int temp = x;
        x = y;
        y = temp;
    }

    if (x % 2 == 0) {
        if (x / 2 == y && z == x / 2) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    } else {
        if (x / 2 == y && z == x / 2 + 1) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
}