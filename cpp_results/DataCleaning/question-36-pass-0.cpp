// Count of ways to distribute N items among 3 people with one person receiving maximum. 
 #include <bits/stdc++.h> 
 using namespace std ;
 int countWays ( int N ) {
 
    // Base case
    if (N <= 2)
        return N;
 
    // Initialize the table with 0
    int table[N+1];
    memset(table, 0, sizeof(table));
 
    // Fill the table
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= i; j++) {
            table[i] += table[i-j];
        }
    }
    return table[N];
 }
 
 // Driver program to test above function
 int main() {
    int N = 5;
    cout << countWays(N) << endl;
    return 0;
 }
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 