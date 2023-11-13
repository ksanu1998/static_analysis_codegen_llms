#include <bits/stdc++.h> 
 using namespace std ;
 void alternateFib ( int n ) {
// Initialize variables
    int a = 0, b = 1, c = 0;

    // Print the first two elements
    cout << a << " " << b << endl;

    // Iterate for n-2 more elements
    for (int i = 2; i < n; i++)
    {
        c = a + b;
        a = b;
        b = c;
        cout << c << " ";
    }

    // End with a newline
    cout << endl;
}

int main()
{
    int n;
    cin >> n;
    alternateFib(n);
    return 0;
}