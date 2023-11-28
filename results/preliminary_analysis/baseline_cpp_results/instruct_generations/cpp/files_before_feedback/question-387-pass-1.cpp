#include <iostream> 
 using std :: cout ;
 void fib ( int n ) {
int a = 0, b = 1, c;
    for (int i = 0; i < n; i++) {
        c = a + b;
        a = b;
        b = c;
        cout << c << " ";
    }
}

int main() {
    int n;
    cout << "Enter the number of terms: ";
    cin >> n;
    fib(n);
    return 0;
}