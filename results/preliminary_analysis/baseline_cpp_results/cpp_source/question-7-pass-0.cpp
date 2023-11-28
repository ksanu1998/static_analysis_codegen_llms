// Check if a graph constructed from an array based on given conditions consists of a cycle or not. 
 #include <bits/stdc++.h> 
 using namespace std ;
 void isCycleExists ( int arr [ ] , int N ) {
 
    // Create a graph from the array
    vector <int> graph [N] ;
    for ( int i = 0 ; i < N ; i++ ) {
        for ( int j = 0 ; j < arr [i] ; j++ ) {
            int x ; cin >> x ;
            graph [i].push_back ( x ) ;
        }
    }
 
    // Create a boolean array to mark visited nodes
    bool visited [N] ;
    for ( int i = 0 ; i < N ; i++ )
        visited [i] = false ;
 
    // Create a boolean array to mark nodes which are part of cycle
    bool partOfCycle [N] ;
    for ( int i = 0 ; i < N ; i++ )
        partOfCycle [i] = false ;
 
    // Call the recursive function to find if a cycle exists
    // in the graph or not
    if ( isCycleExistsUtil ( graph, visited, partOfCycle, 0 ) )
        cout << "Yes" ;
    else
        cout << "No" ;
}
 
// A recursive function to check if a cycle exists in the graph
// or not
bool isCycleExistsUtil ( vector <int> graph [ ], bool visited [ ], bool partOfCycle [ ], int node ) {
 
    // Mark the current node as visited and part of cycle
    visited [node] = true ;
    partOfCycle [node] = true ;
 
    // Recur for all the vertices adjacent to this vertex
    for ( int i = 0 ; i < graph [node].size ( ) ; i++ ) {
        int x = graph [node] [i] ;
        if (!visited [x] ) {
            if ( isCycleExistsUtil ( graph, visited, partOfCycle, x ) )
                return true ;
        }
        else if ( partOfCycle [x] )
