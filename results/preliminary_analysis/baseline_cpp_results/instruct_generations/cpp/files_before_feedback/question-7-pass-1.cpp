#include <bits/stdc++.h> 
 using namespace std ;
 void isCycleExists ( int arr [ ] , int N ) {
// Create a vector to store the graph
    vector<vector<int>> graph(N);

    // Loop through the array and add edges to the graph
    for (int i = 0; i < N; i++) {
        int u = arr[i];
        for (int j = i + 1; j < N; j++) {
            int v = arr[j];
            if (u < v) {
                graph[u].push_back(v);
            }
        }
    }

    // Check if the graph has a cycle
    bool hasCycle = false;
    for (int i = 0; i < N &&!hasCycle; i++) {
        if (graph[i].size() > 0) {
            hasCycle = true;
        }
    }

    // Print the result
    if (hasCycle) {
        cout << "The graph has a cycle." << endl;
    } else {
        cout << "The graph does not have a cycle." << endl;
    }
}