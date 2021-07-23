def RadixSort(A):
	n=len(A)
	maxelement=max(A)
	digits=len(str(maxelement))
	l=[]
	bins=[l]*10
	#for passing purpose
	#based on the number of digits
	for i in range(digits):
		#for traversing through the array
		for j in range(n):
			e=int((A[j]/pow(10,i))%10)
			if len(bins[e]) > 0:
				bins[e].append(A[j])
			else:
				bins[e]=[A[j]]
		k=0
		#for traversing through the
		#added elements in bins
		for x in range(10):
			#checking if already elemens are there
			#in the bins
			if len(bins[x]) > 0:
				#for traversing through the added 
				#elements of bins
				for y in range(len(bins[x])):
					#storing the elements in k
					#and remove the element from bins
					A[k]=bins[x].pop(0)
					k+=1
A=[452,14,250,24,5,3,0,456]
print("Original Array :", A)
RadixSort(A)
print("Sorted Array :", A)					
