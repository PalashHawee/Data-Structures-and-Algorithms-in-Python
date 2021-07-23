#Count Sort takes O(n) time and
#space complexity is O(n) it's space consuming

def CountSort(A):
	n=len(A)
	maxSize=max(A)
	countArray=[0]*(maxSize+1)
	#for iterating through array A
	#and placing the elements in countArray
	for i in range(n):
		countArray[A[i]]+=1
	i=0 #for countArray
	j=0	#for Original array A
	while i<maxSize+1:
		if countArray[i]>0:
			A[j]=i
			j+=1
			countArray[i]-=1
		else:
			i+=1	
A=[5,7,8,2,3,4,10]
print("Original Array: ",A)
CountSort(A)
print("Sorted Array :",A)