#Two number Sum
#time O(nlogn)| Space O(1)
def twoNumberSum(array, targetSum):
   
    array.sort()
	left=0
	right=len(array)-1
	while left<right:
		currentSum=array[left]+array[right]
		if currentSum==targetSum:
			return [array[left],array[right]]
		elif currentSum < targetSum:
			left+=1
		elif currentSum > targetSum:
			right-=1
	return []	

#Time O(n) n is the number of input array | Sapce O(n) for extra space in dictionary
def twoNumberSum(array, targetSum):
    # Write your code here.
    nums={}
	for num in array:
		potentialMatch=targetSum-num
		if potentialMatch in nums:
			return[potentialMatch,num]
		else:
			nums[num]=True
	return []	

#Time O(n^2) using double for loop | Space O(1)
def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)-1):
		firstNum=array[i]
		for j in range(i+1,len(array)):
			secondNum=array[j]
			if firstNum+secondNum==targetSum:
				return[firstNum,secondNum]
	return []		


