# Author  MD. ABDUL MOMIN
#Islamic university, kushtia
#momin.ice16@gmail.com

#Binary search is  one of most useful algorithm for finding index of searching value. But precondition is array should be sorted . TIme complexity log2(n) 
#Date: 16-03-18 


def binaySearch(arr,low,high,value): #binary search part
	
	while low<=high:
		mid = int((low+high)/2)  #Find mid position of sorted arry

		if arr[mid]<value:      #if value is in 2nd half
			low=mid+1
		elif arr[mid]>value:    #if value is in first half
			high=mid-1
		else:
			low=mid
			high=mid-1
	return low          #Return index of that value if exists or return upperbound position of that value

arr = [4,5,6,7,9,10,11,23]      #A sorted array 
print(binaySearch(arr,0,len(arr)-1,12)) #value = 9 index =4 #value=12 index=7 as upperbound
