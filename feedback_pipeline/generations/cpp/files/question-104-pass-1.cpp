#include <bits/stdc++.h> 
 using namespace std ;
 bool check ( int X , int K ) {
int count = 0;
for (int i = 1; i <= X; i++)
{
    if (isPrime(i))
        count++;
    if (count == K)
        return true;
}
return false;