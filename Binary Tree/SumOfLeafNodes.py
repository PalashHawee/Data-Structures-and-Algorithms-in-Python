#Finding sum of leaf Nodes from leftmost branch to its rightmost branch
# time and space O(n)
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums=[]
	calculateBranchSums(root,0,sums)
	return sums
	
def calculateBranchSums(node,runningsum,sums):
	if node is None:
		return
	newRunningSum=runningsum+node.value
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return
	calculateBranchSums(node.left,newRunningSum,sums)
	calculateBranchSums(node.right,newRunningSum,sums)
	
