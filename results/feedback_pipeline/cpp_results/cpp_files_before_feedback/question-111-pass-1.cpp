#include <bits/stdc++.h> 
 using namespace std ;
 void countOfGreaterElements ( int arr [ ] , int n ) {
// Initialize a count array with all elements as 0
    int count[n] = {0};

    // Iterate through the array and increment the count of
    // greater elements for each element
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] < arr[j])
                count[i]++;
        }
    }

    // Print the count array
    for (int i = 0; i < n; i++)
        cout << count[i] << " ";
    cout << endl;
}

int main() {
    int arr[] = {1, 3, 5, 7, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    countOfGreaterElements(arr, n);
    return 0;
}