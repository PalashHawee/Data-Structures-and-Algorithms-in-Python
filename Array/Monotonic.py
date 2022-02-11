# Return an array if it's Monotonic or not

#Time O(n) | space O(1)

def isMonotonic(array):
   
    isNonDecreasing=True
	isNonIncreasing=True
	
	for i in range(1,len(array)):
		if array[i] < array[i-1]:
			isNonDecreasing=False
		if array[i] > array[i-1]:
			isNonIncreasing=False
			
	return isNonDecreasing or isNonIncreasing		
