#Write a function that takes in a positive integers
#and return the max sum of non-adjacent elems in array

#Time O(N)| Space O(1) n length of the input array
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not len(array):
		return 0
	elif len(array)==1:
		return array[0]
	second=array[0]
	first=max(array[0],array[1])
	for i in range(2,len(array)):
		current=max(first, second+array[i])
		second=first
		first=current
	return first
#2nd Solution
#Time O(N)| Space O(N)
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not len(array):
		return 0
	elif len(array)==1:
		return array[0]
	maxSums=array[:]
	maxSums[1]=max(array[0],array[1])
	for i in range(2,len(array)):
		maxSums[i]=max(maxSums[i-1], maxSums[i-2]+array[i])
	return maxSums[-1]	

