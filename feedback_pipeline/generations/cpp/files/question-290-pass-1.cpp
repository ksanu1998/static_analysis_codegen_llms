#include <iostream> 
 using namespace std ;
 void Sum_upto_nth_Term ( int n ) {
int sum = 0;
for (int i = 2, j = 3; i <= n; i++, j += 2)
{
    sum += i * j;
}
cout << "Sum of first " << n << " terms of the series is: " << sum << endl;