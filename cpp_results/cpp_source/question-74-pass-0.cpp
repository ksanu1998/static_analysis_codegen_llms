// Program to check if N is a Pentadecagonal Number. 
 #include <bits/stdc++.h> 
 using namespace std ;
 bool isPentadecagon ( int N ) {
 
    int n = 1;
    int sum = 0;
    while (n <= N) {
        sum += n;
        n += 5;
    }
    if (sum == N) {
        return true;
    }
    return false;
}
int main() {
    int N;
    cin >> N;
    if (isPentadecagon(N)) {
        cout << "Yes";
    } 