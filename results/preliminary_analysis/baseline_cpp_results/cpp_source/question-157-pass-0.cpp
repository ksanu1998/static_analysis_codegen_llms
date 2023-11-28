// Program to find the number from given holes. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void printNumber ( int holes ) {
 
    int n = 10;
    int arr[n];
    for (int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }
    int i = 0;
    int j = n - 1;
    while (i <= j) {
        if (holes == arr[i]) {
            cout << holes << " found at index " << i << endl;
            return;
        }
        if (holes == arr[j]) {
            cout << holes << " found at index " << j << endl;
            return;
        }
        if (holes < arr[i]) {
            j = j - 1;
        }
        if (holes > arr[j]) {
            i = i + 1;
        }
    }
    cout << "Not found" << endl;
}
int main () {
    int holes;
    cout << "Enter the number of holes: ";
    cin >> holes;
    printNumber (holes);
    return 0;
}


























































































































































































































