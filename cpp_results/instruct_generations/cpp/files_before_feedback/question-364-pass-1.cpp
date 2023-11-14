#include <iostream> 
 using namespace std ;
 int solve ( int x ) {
int count = 0;
for (int i = 10; i <= 99; i++)
{
    if (i % 10 == i / 10)
    {
        count++;
    }
}
return count;