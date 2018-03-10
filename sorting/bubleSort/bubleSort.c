/*

Author: Jony Roy
Email: jonyroyice@gmail.com
Date: 10-03-2018

Description:
    Buble Sort Algorithm Implementation in C

*/

#include<stdio.h>
#include<string.h>
int main()
{
    int n,m[100],i,temp,j;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    scanf("%d",&m[i]);
    for(i=1;i<n;i++)
    {
        for(j=1;j<=n-i;j++)
        {
            if(m[j]>m[j+1])
            {
                temp=m[j];
                m[j]=m[j+1];
                m[j+1]=temp;
            }
        }
    }
    for(i=n;i>=1;i--)
    printf("%d ",m[i]);
    return 0;
}