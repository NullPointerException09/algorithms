# Author  MD. ABDUL MOMIN
#Islamic university, kushtia
#momin.ice16@gmail.com
#Date: 22-03-18 

#Here we  will find of of a range for each query.

#There are three part of segment tree Build Tree, update Tree and queury

#This program is written for  minimum value in ranges  


#Time complexity:
# Build Tree  O(N) 
# Modified tree O(log(N))
# query from array O(log(N))


builtTree=[100000]*100000     # This variable is declared globally. and initialize builtTree with infinity value 
#here we assume arr value is lower than 100000 and maximum Tree node is lower than 100000


def buildTree(arr,node,start,end):

	mid = int((start+end)/2)
	if start == end:
		builtTree[node]=arr[start]  #assign array value into Tree
		return
	else:
		L = buildTree(arr,node*2,start,mid)     #Left subtree
		R = buildTree(arr,node*2+1,mid+1,end)   #RIght subtree
		builtTree[node]= min(builtTree[node*2],builtTree[node*2+1]) #assign minimum value from left and right subtree to tree's parent node


#--------------------------------------
# for modify value , it may me add,subtract or muliple
def updateTree(node,start,end,p,q,val):
	if q<start or end<p:
		return
	if (p<=start and end<=q) and (start==end):
		builtTree[node] +=val    #modify value
		return
	mid=int((start+end)/2)
	updateTree(node*2,start,mid,p,q,val)  #update left subtree
	updateTree(node*2+1,mid+1,end,p,q,val) #update right subtree

#-----------------------------------------
#This section is used for find minimum value in given range p and q 
def query(node,start,end,p,q):
	if q<start or end<p:
		return 100000
	if p<=start and end<=q:
	 	return builtTree[node]
	mid=int((start+end)/2)
	ans=min(query(node*2,start,mid,p,q),query(node*2+1,mid+1,end,p,q))

	return ans


#Main function 
#Given array value
arr = [1,3,4,5,6,7,5,4,3] 


buildTree(arr,1,0,8) #make a tree with arr value

print(query(1,0,len(arr)-1,1,4)) #find minimum value from index 1 to 4

#here ans is 3 


updateTree(1,0,len(arr)-1,2,4,-8)      #modify value with adding -8 to index from  2 to 4 
# modified arr = 1,3,-4,-3,-2,7,5,4,3


print(query(1,0,len(arr)-1,2,6))   # finding minimum value from index 2 to 6

#here ans is -4 because of modify array







	






