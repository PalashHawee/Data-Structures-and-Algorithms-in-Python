#Time O(n) and space O(lon(n))
def maxPathSum(tree):
    # Write your code here.
    _,maxSum=findMaxSum(tree)
	return maxSum
def findMaxSum(tree):
	if tree is None:
		return (0,float("-inf"))
	leftMaxSumAsBranch,leftMaxPathSum=findMaxSum(tree.left)
	rightMaxSumAsBranch,rightMaxPathSum=findMaxSum(tree.right)
	maxChildSumAsBranch=max(leftMaxSumAsBranch,rightMaxSumAsBranch)
	value=tree.value
	maxSumAsBranch=max(maxChildSumAsBranch+value,value)
	maxSumAsRootNode=max(leftMaxSumAsBranch+value+rightMaxSumAsBranch,maxSumAsBranch)
	maxPathSum=max(leftMaxPathSum,rightMaxPathSum,maxSumAsRootNode)
	return(maxSumAsBranch,maxPathSum)
	