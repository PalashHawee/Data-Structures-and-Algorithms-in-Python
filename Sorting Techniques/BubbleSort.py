#Bubble Sort
#max time O(n^2) if list not sorted
#Min time O(n) if list is already sorted
def BubbleSort(arr):
	n=len(arr)
	#for no of passes
	for i in range(n-1):
		#for comparision of elements and 
		#every time comparision gets less so (n-1-i)
		for j in range(n-1-i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[10,45,2,3,9,50,7]
BubbleSort(arr)
print("Sorted Array is :")
for i in range(len(arr)):
	print("%d"%arr[i])				
