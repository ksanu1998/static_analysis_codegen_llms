#include <bits/stdc++.h> 
 using namespace std ;
 void getXandYintercept ( int P [ ] , int Q [ ] ) {
// Calculate the slope of the line passing through the given points
    double slope = (double)(P[1] - P[0]) / (Q[1] - Q[0]);

    // Calculate the y-intercept of the line
    double yIntercept = P[0] - slope * Q[0];

    // Calculate the x-intercept of the line
    double xIntercept = Q[0] - slope / yIntercept;

    // Print the x and y intercepts
    cout << "X intercept: " << xIntercept << endl;
    cout << "Y intercept: " << yIntercept << endl;
}

int main() {
    // Test case 1: Line passing through (1, 1) and (2, 3)
    int P[2] = {1, 1};
    int Q[2] = {2, 3};
    getXandYintercept(P, Q);

    // Test case 2: Line passing through (0, 0) and (1, 1)
    int R[2] = {0, 0};
    int S[2] = {1, 1};
    getXandYintercept(R, S);

    // Test case 3: Line passing through (0, 0) and (2, 4)
    int T[2] = {0, 0};
    int U[2] = {2, 4};
    getXandYintercept(T, U);

    return 0;
}