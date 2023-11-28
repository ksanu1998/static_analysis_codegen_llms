#include <iostream> 
 using namespace std ;
 void checkSolution ( int a , int b , int c ) {
// Check if the discriminant is positive
    if ( b * b - 4 * a * c < 0 ) {
        cout << "No real solutions" << endl ;
    }
    // Check if the discriminant is equal to zero
    else if ( b * b - 4 * a * c == 0 ) {
        cout << "One real solution" << endl ;
    }
    // Check if the discriminant is positive
    else {
        cout << "Two real solutions" << endl ;
    }
}

int main () {
    int a, b, c ;
    cout << "Enter the values of a, b and c : " << endl ;
    cin >> a >> b >> c ;
    checkSolution ( a, b, c ) ;
    return 0 ;
}