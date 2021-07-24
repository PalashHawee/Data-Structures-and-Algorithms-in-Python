#Takes O(nlogn) time n for no of elements
#and logn since it goes thorugh successive division n/2

def ShellSort(A):
	n=len(A)
	gap=n//2
	while gap>0:
		i=gap
		while i<n:
			temp=A[i]#holding the elements of array
			j=i-gap
			while j>=0 and A[j]>temp:
				A[j+gap]=A[j] #moving j to next index
				j=j-gap
			A[j+gap]=temp
			i=i+1
		gap=gap//2
		
A=[45,12,5,3,1,4,10,50,42]
print("Original Array :",A)
ShellSort(A)
print("Sorted Array :",A)				