#include <bits/stdc++.h> 
 using namespace std ;
 void printDiagonalTraversal ( vector < vector < int > > & nums ) {
// Write your code here
    vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
        result.push_back(nums[i][i]);
    }
    return result;
}