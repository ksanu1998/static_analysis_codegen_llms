#include <bits/stdc++.h>
using namespace std;
void findEquation(int a, int b, int c) {
    // Calculate the discriminant of the equation
    int discriminant = (b * b) - (4 * a * c);
    // Check if the equation has real roots
    if (discriminant > 0) {
        // Calculate the two solutions
        int x1 = (-b + sqrt(discriminant)) / (2 * a);
        int x2 = (-b - sqrt(discriminant)) / (2 * a);
        // Print the solutions
        cout << "The equation has two real roots: " << x1 << " and " << x2 << endl;
    } else if (discriminant == 0) {
        // Calculate the single solution
        int x = -b / (2 * a);
        // Print the solution
        cout << "The equation has a single real root: " << x << endl;
    } else {
        // The equation has no real roots
        cout << "The equation has no real roots." << endl;
    }
}
int main() {
    // Test the function with different values of a, b, and c
    findEquation(1, 2, 3);
    findEquation(2, 3, 4);
    findEquation(3, 4, 5);
    return 0;
}