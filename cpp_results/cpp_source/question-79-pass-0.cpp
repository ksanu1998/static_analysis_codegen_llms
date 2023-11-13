// Program to check if N is a Concentric Hexagonal Number. 
 #include <bits/stdc++.h> 
 using namespace std ;
 bool isConcentrichexagonal ( int N ) {
 
    int i = 1;
    while (i * (i * 2 - 1) <= N) {
        i++;
    }
    return (i * (i * 2 - 1) == N);
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        if (isConcentrichexagonal(N))
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    