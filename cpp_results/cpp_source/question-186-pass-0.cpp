// Generate an Array in which count of even and odd sum sub. 
 #include <algorithm> 
 #include <iostream> 
 using namespace std ;
 void CreateArray ( int N , int even , int odd ) {
 
    int arr[N];
    int sum = 0;
    int evenSum = 0;
    int oddSum = 0;
    int i;
    for ( i = 0 ; i < N ; i++ ) {
        arr[i] = rand() % 100;
        sum += arr[i];
        if ( arr[i] % 2 == 0 ) {
            evenSum += arr[i];
        }
        else {
            oddSum += arr[i];
        }
    }
    cout << "Sum of all elements is " << sum << endl;
    cout << "Sum of even elements is " << evenSum << endl;
    cout << "Sum of odd elements is " << oddSum << endl;
    cout << "Sum of even elements is " << evenSum << endl;
    cout << "Sum of odd elements is " << oddSum << endl;
    cout << "Sum of even elements is " << evenSum << endl;
    cout << "Sum of odd elements is " << oddSum << endl;
    cout << "Sum of even elements is " << evenSum << endl;
    cout << "Sum of odd elements is " << oddSum << endl;
    cout << "Sum of even elements is " << evenSum << endl;
    cout << "Sum of odd elements is " << oddSum << endl;
    cout << "Sum of even elements is " << evenSum << endl;
    cout << "Sum of odd elements is " << oddSum << endl;
    cout << "Sum of even elements is " << evenSum << endl;
    cout << "Sum of odd elements is " << oddSum << endl;
    cout << "Sum of even elements is " << evenSum << endl;
    cout << "Sum of odd elements is " << oddSum << endl;
    cout << "Sum of even elements is " << evenSum << endl;
    cout << "Sum of odd elements is " << oddSum << endl;
    cout << "Sum of even elements is " << even