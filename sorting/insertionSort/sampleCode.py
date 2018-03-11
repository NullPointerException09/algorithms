# Author  MD. ABDUL MOMIN
#Islamic university, kushtia
#momin.ice16@gmail.com

####Insertion sort implementation with python####
## we sort this list in assending order
#Date: 11-03-18 

numArray = [5,4,2,6,4,3,5,6,7,3,6,2] ##number stored in a list

for index in range(len(numArray)): ## accessing the array 
	key = numArray[index]
	index1 = index-1
	while index1>=0 and numArray[index1]>key: ## compare through inserting process 
		numArray[index1+1] = numArray[index1]
		index1  = index1-1
	
	numArray[index1+1]=key	

print (numArray[0:len(numArray)]) ##show sorted array 

	

    