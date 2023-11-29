#include <bits/stdc++.h> 
 using namespace std ;
 #define ull  unsigned long long 
 void findCount ( int n ) {
// Initialize the count of each character to 0
    int countA = 0, countB = 0, countC = 0;

    // Loop for the given number of seconds
    for (int i = 0; i < n; i++)
    {
        // Increment the count of each character based on the reproduction rate
        countA += (i + 1) / 2;
        countB += (i + 1) / 3;
        countC += (i + 1) / 4;
    }

    // Print the final count of each character
    cout << "Count of A: " << countA << endl;
    cout << "Count of B: " << countB << endl;
    cout << "Count of C: " << countC << endl;
}

int main()
{
    // Take input for the number of seconds
    int n;
    cin >> n;

    // Call the function to find the count of each character
    findCount(n);

    return 0;
}