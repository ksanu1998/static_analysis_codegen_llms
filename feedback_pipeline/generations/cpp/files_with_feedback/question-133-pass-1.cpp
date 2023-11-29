#include <bits/stdc++.h>
using namespace std;
void solve(int A, int B) {
    // Calculate the vertex of the parabola
    int vertex_x = (B*B - 4*A*C) / (2*A);
    int vertex_y = (-B + sqrt(B*B - 4*A*C)) / (2*A);
    // Calculate the distance between the vertex and the point (A, B)
    int distance = sqrt((vertex_x - A)*(vertex_x - A) + (vertex_y - B)*(vertex_y - B));
    // Check if the point is on the parabola
    if (distance <= 1) {
        cout << "The point (A, B) is on the parabola." << endl;
    } else {
        cout << "The point (A, B) is not on the parabola." << endl;
    }
}
int main() {
    int A, B;
    cin >> A >> B;
    solve(A, B);
    return 0;
}