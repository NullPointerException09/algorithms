# Author  MD. ABDUL MOMIN
#Islamic university, kushtia
#momin.ice16@gmail.com

#Binary search is  one of most useful algorithm for finding index of searching value. But precondition is array should be sorted . TIme complexity log2(n) 
#Date: 18-03-18 


def findIndexOfSearchingValue(arr,searchingValue):
	for index in range(0,len(arr),1):
		if searchingValue==arr[index]:
			return index+1

arr = []

n = int(input("How many value Do you have: "))
for i in range(0,n,1):
	val= int(input())
	arr.append(val)

searchingValue = int(input("Input the searching value: "))
pos =  findIndexOfSearchingValue(arr,searchingValue)

print("The position of searching value in array is  %d"%pos)

