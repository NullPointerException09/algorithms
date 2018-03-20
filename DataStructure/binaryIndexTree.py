# Author  MD. ABDUL MOMIN
#Islamic university, kushtia
#momin.ice16@gmail.com
#Date: 20-03-18 

#Binary index Tree is used for finding range of values. Binary index Tree and 
#segment tree are used for same perpose, Time complexity of both algorithm are same but binary index Tree is used less space
# Time complextity O(nLog(n));

#-------------------------------------------
#This section finds summation of 0 to index
def getSum(bTree,index):
	sum=0
	index = index +1
	while index>0:
		sum =sum+ bTree[index]
		#Find parent of index child
		index = index-(index&(-index)) 
	return sum

#-----------------------------------------------

#This section is used for update value into binary index tree
def update(bTree,n,index,val):
	index = index+1
	while index<=n:
		bTree[index]+=val
		index+=(index&(-index)) #Find child of index parent
#------------------------------------------------------
#Build Tree 
def buildTree(arr,n):
	bTree = [0]*(n+1)
	for i in range(0,n,1):
		bTree.append(0)
	for i in range(0,n,1):
		update(bTree,n,i,arr[i])
	return bTree

#Main function 

n = int(input("How many values you want to input "));

arr = []
BuiltTree = []
for i in range(0,n,1):
	val=int(input())
	arr.append(val)
BuiltTree = buildTree(arr,n)


#summation between two ranges p and q. Range start from index 1
p = int(input("Enter the value of P "))   
q = int(input("Enter the vale of q "))

if p>q:
	p,q=q,p

pvalue = int(getSum(BuiltTree,p-2))
qvalue = int(getSum(BuiltTree,q-1))
print("Summation of p and q ranges is: ")
print(qvalue-pvalue)





