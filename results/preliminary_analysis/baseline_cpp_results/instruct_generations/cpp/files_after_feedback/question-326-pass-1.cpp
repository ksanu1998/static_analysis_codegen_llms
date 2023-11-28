#include <bits/stdc++.h>
using namespace std;
double bellman(int s, int d, vector<pair<pair<int, int>, double>> ed, int n) {
    double dist[n];
    for (int i = 0; i < n; i++) {
        dist[i] = inf;
    }
    dist[s] = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < ed.size(); j++) {
            int u = ed[j].first.first;
            int v = ed[j].first.second;
            double w = ed[j].second;
            if (dist[u]!= inf && dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
            }
        }
    }
    return dist[d];
}