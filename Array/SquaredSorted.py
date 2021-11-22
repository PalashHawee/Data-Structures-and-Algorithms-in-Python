#Squared Sorted Array
#Brute force appraoch
#O(n logn) time | O (n) space

def sortedSquaredArray(array):
  
    sortedSquares=[0 for _ in array ]
	for i in range(len(array)):
		value=array[i]
		sortedSquares[i]=value*value
		
	sortedSquares.sort()
	return sortedSquares

#optimal solution
#O(n) time | O(n) space
def sortedSquaredArray(array):
   
    sortedSquares=[0 for _ in array]
	smallerValueIdx=0
	largerValueIdx=len(array)-1
	
	for i in reversed(range(len(array))):
		smallerValue=array[smallerValueIdx]
		largerValue=array[largerValueIdx]
		
		if abs(smallerValue) > abs(largerValue):
			sortedSquares[i]=smallerValue*smallerValue
			smallerValueIdx+=1
		else:
			sortedSquares[i]=largerValue*largerValue
			largerValueIdx-=1
	return sortedSquares		
				

