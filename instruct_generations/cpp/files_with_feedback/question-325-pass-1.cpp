#include <bits/stdc++.h>
#define inf 100000000
using namespace std;
double smPath(int s, int d, vector<pair<pair<int, int>, int>> ed, int n, int k) {
    // Create a 2D array to store the shortest distances
    double dist[n][k];
    // Initialize all distances as infinite
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < k; j++) {
            dist[i][j] = inf;
        }
    }
    // Distance from source to source is 0
    dist[s][0] = 0;
    // Loop for k times
    for (int i = 1; i <= k; i++) {
        // Loop for all edges
        for (int j = 0; j < ed.size(); j++) {
            int u = ed[j].first.first;
            int v = ed[j].first.second;
            int w = ed[j].second;
            // Check if the distance from source to current node is less than the distance from source to current node plus the weight of the edge
            if (dist[u][i - 1]!= inf && dist[u][i - 1] + w < dist[v][i]) {
                dist[v][i] = dist[u][i - 1] + w;
            }
        }
    }
    // Return the shortest distance from source to destination
    return dist[d][k - 1];
}