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
    int numberOfItems,m[100],i,temp,j;
    scanf("%d",&numberOfItems);
    for(i=1;i<=numberOfItems;i++)
    scanf("%d",&m[i]);
    for(i=1;i<numberOfItems;i++)
    {
        for(j=1;j<=numberOfItems-i;j++)
        {
            if(m[j]>m[j+1])
            {
                temp=m[j];
                m[j]=m[j+1];
                m[j+1]=temp;
            }
        }
    }
    for(i=numberOfItems;i>=1;i--)
    printf("%d ",m[i]);
    return 0;
}