#include <iostream>
#include<time.h>
using namespace std;
void printMaxActivities(int s[], int f[], int n)
{
    int i, j;
    cout <<"Following activities are selected "<< endl;
    i = 0;
    cout <<" "<< i;
    for (j = 1; j < n; j++)
    {
        if (s[j] >= f[i])
        {
            cout <<" " << j;
            i = j;
        }
    }
}
int main()
{
    clock_t start_t, end_t, total_t;
    start_t = clock();
    int s[] =  {1, 3, 0, 5, 8, 5};
    int f[] =  {2, 4, 6, 7, 9, 9};
    int n = sizeof(s)/sizeof(s[0]);
    printMaxActivities(s, f, n);
    total_t = (double)(start_t);
    cout << "Total time required \n"<<total_t;
    return 0;

}
