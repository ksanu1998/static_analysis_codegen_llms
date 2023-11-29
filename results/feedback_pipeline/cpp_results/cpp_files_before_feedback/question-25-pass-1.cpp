#include <bits/stdc++.h> 
 using namespace std ;
 void findTemperature ( int x , int y , int s ) {
// Calculate the average temperature
    int avg = s / 5;

    // Initialize the missing temperature
    int missing = 0;

    // Loop through the given temperatures
    for ( int i = 0; i < 5; i++ ) {
        // If the current temperature is not the average, then it is the missing temperature
        if ( x[i]!= avg ) {
            missing = x[i];
            break;
        }
    }

    // Print the missing temperature
    cout << "The missing temperature is: " << missing << endl;
}

int main() {
    // Test case 1:
    int x[] = {10, 20, 30, 40, 50};
    int s = 150;
    findTemperature(x, s);

    // Test case 2:
    int x[] = {10, 20, 30, 40, 50};
    int s = 160;
    findTemperature(x, s);

    // Test case 3:
    int x[] = {10, 20, 30, 40, 50};
    int s = 170;
    findTemperature(x, s);

    return 0;
}