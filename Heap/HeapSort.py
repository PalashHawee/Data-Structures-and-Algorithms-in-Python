from Deleting import Heap
#Time for inserting is O(nlogn) where n are elements
#Time for deleting is O(nlogn) where n is no of nodes deleted
#Function for performing HeapSort
def heapSort(A):
	H=Heap()
	n=len(A)
	for i in range(n):
		H.Insert(A[i])
	#For performing Deletion
	#and store them back in heap to Perform HeapSort
	k=n-1
	for i in range(H.currentSize):
		A[k]=H.DeleteMax() #deleting and storing them back at K index
		k=k-1
A=[40,12,56,4,2,8,9,6,55]
print("Original Array:",A)
heapSort(A)
print("Sorted Array:",A)		
