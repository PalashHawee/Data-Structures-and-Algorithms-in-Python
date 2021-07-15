#Algorithm for Selection Sort
#Time O(n^2) since it's comaparison based sorting
def selectionSort(arr):
	n=len(arr)
	
	#for no of passes
	for i in range(0,n-1):
		#for iterating through array using j
		j=k=i
		for j in range(i, n):
			if arr[j]<arr[k]:
			#bring k upon j
				k=j
		arr[i],arr[k]=arr[k],arr[i]
		
arr=[12,45,8,5,6,1,3]
selectionSort(arr)
for i in range(len(arr)):
	print("%d"%arr[i])			