#include <bits/stdc++.h> 
 using namespace std ;
 vector < int > restore ( int arr [ ] , int N ) {
 vector < int > result ;
 int count1 = 1 ;
 set < int > s ;
 for ( int i = 0 ;
 i < N ;
 i ++ ) {
 s . insert ( arr [ i ] ) ;
 if ( s . size ( ) == count1 ) {
 result . push_back ( arr [ i ] ) ;
 count1 ++ ;
 } } return result ;
 } void print_result ( vector < int > result ) {
#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<int> restore(int arr[], int N) {
    vector<int> result;
    int count1 = 1;
    set<int> s;
    for (int i = 0; i < N; i++) {
        s.insert(arr[i]);
        if (s.size() == count1) {
            result.push_back(arr[i]);
            count1++;
        }
    }
    return result;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int N = sizeof(arr) / sizeof(arr[0]);
    vector<int> result = restore(arr, N);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    return 0;
}