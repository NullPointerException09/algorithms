/******************************************
          Mobarak Hosen Shakil
        ICE, Islamic University
     ID: mhiceiuk(all), 29698(LOJ)
   E-mail: mhiceiuk @ (Gmail/Yahoo/FB)
 Blog: https://iuconvergent.wordpress.com
*******************************************/
#include<bits/stdc++.h>
using namespace std;
#define IOS ios_base::sync_with_stdio(0);cin.tie(0)
#define LL long long int
#define ULL unsigned LL

const int inf=1<<30;
const LL INF=1e18;
const int MOD=1e9+7;

int main()
{
    int n, v;
    scanf("%d", &n);
    int arr[n+2];
    memset(arr, 0, sizeof arr);

    for(int i=0; i<n; i++)
    {
        scanf("%d", &v);
        arr[v]++;          
    }

    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=arr[i]; j++)
        {
            printf("%d ", i);         // Print each unique value as counted time
        }
    }
    printf("\n");
    return 0;
}

