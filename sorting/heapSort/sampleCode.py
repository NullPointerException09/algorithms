# Author  MD. ABDUL MOMIN
#Islamic university, kushtia
#momin.ice16@gmail.com

####Heap sort implementation with python####
## we sort this list in assending order
#Date: 16-03-18 

##Build head using Max heap rearrange the value as binary tree propertics root>left and right

def buildHeap(arr,n,i):
	largest = i;
	left = 2*i+1;
	right =2*i+2;
	if right<n and arr[largest]<arr[right]: 
		largest = right
	if left<n and arr[largest]<arr[left]:
		largest = left
	if i!=largest:
		arr[i],arr[largest]= arr[largest],arr[i] #swap
		buildHeap(arr,n,largest)
#Main part for HeapSort
def heapSort(arr):
	n = len(arr)
	for i in range(n,-1,-1): #Here we build Tree with high level to low approach
		buildHeap(arr,n,i)
	for i in range(n-1,0,-1):#For Exacting Top value we use bottom to top
		arr[i],arr[0] = arr[0],arr[i] #swap 
		buildHeap(arr,i,0)

arr = [12,11,13,6,4,3]
heapSort(arr)
n=len(arr)
print("sorted array is ")
for i in range(n):
	print("%d" %arr[i]) #3,4,6,13,11,12

##*** For ordering desending order we have to find lower value in BuildHeap subpart