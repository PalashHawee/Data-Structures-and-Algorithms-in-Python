#Write a function to return the max sum of the input sub array
#Time O(n)/ space O(1)

def kadanesAlgorithm(array):
    
    maxEndingHere=array[0]
	maxSoFar=array[0]
	for i in range(1,len(array)):
		num=array[i]
		maxEndingHere=max(num,maxEndingHere+num)
		maxSoFar=max(maxSoFar,maxEndingHere)
	return maxSoFar	
