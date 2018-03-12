/*
Author: Mehedi Hasan Ronee
github_id: ronee12
email: ronikushtia@gmail.com
Date: 11.03.2018

Program Name: Selection Sort
Time Complexity: O(n^2)

*/

#include<bits/stdc++.h>
using namespace std;
int main(){

    int arr[100],number;
    //Input
    scanf("%d",&number);
    for(int index=0;index<number;index++){
        scanf("%d",&arr[index]);
    }

    //Algorithm
    for(int index=0;index<number-1;index++){
        int minimum=index;
        for(int j=index+1;j<number;j++){
            if(arr[j]<arr[minimum])
                minimum=j;
        }
        swap(arr[index],arr[minimum]);
    }

    //Output
    for(int index=0;index<number;index++)
        printf("%d ",arr[index]);

}



