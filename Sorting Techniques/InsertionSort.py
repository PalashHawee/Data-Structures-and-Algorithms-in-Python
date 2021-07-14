#Insertion sort Max time O(n^2) min time O(n) 
#if list is already sorted

def InsertionSort(arr):
	n=len(arr)
	for i in range(1,n):
		j=i-1
		x=arr[i]
		while(j>-1 and arr[j]>x):
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=x	

arr=[10,20,45,2,6,20]
InsertionSort(arr)
for i in range(len(arr)):
	print("%d"% arr[i])		