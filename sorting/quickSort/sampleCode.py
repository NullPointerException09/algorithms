# Author  MD. ABDUL MOMIN
#Islamic university, kushtia
#momin.ice16@gmail.com

####Quick sort implementation with python####
## we sort this list in assending order
#Date: 13-03-18 


##This section determines the location of last element
def partition(arr,low,high):
	i=low-1
	pivot = arr[high]
	for j in range(low,high):
		if arr[j]<=pivot:
			i=i+1
			arr[i],arr[j]=arr[j],arr[i]
	arr[i+1],arr[high]=arr[high],arr[i+1]
	
	return (i+1)
#This function devides into two subpart left subpart and right subpart 
def quickSort(arr,low,high):
	if low<high:
		mid = partition(arr,low,high) #location of last element

		quickSort(arr,low,mid-1)  #left subpart
		quickSort(arr,mid+1,high) #Right subpart
arr = []   #Declare a list named arr 

print ('How many numbers should be sorted  ')
n = int(input())           #converts string to integer

for index in range(0,n): 
	num = int(input())        #input arr element
	arr.append(num)         # insert into arr
#arr = [6,4,3,6,4,1,3,6,7,4,6,7,3,1]

quickSort(arr,0,n-1)     #call quickSort module
print (arr)      #print The sorted arr