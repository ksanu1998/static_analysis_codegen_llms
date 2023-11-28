#include <iostream>
#include <string>
using namespace std;
void quadrant(string s) {
    int real = 0;
    int imag = 0;
    int quadrant = 0;
    // Extract the real and imaginary parts of the complex number
    // from the input string
    real = stoi(s.substr(0, s.find("+")));
    imag = stoi(s.substr(s.find("+") + 1, s.length() - 1));
    // Calculate the quadrant of the complex number
    if (real > 0 && imag > 0) {
        quadrant = 1;
    } else if (real < 0 && imag > 0) {
        quadrant = 2;
    } else if (real < 0 && imag < 0) {
        quadrant = 3;
    } else if (real > 0 && imag < 0) {
        quadrant = 4;
    }
    // Print the quadrant of the complex number
    cout << "Quadrant of " << s << " is " << quadrant << endl;
}
int main() {
    string s;
    cin >> s;
    quadrant(s);
    return 0;
}