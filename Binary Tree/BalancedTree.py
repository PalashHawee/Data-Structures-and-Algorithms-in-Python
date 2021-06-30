#Height Balanced Binary tree
#Time O(n) and space O(h) where h is the height of the tree

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
	def __init__(self,isBalanced,height):
		self.isBalanced=isBalanced
		self.height=height
def heightBalancedBinaryTree(tree):
   
	treeInfo=getTreeInfo(tree)
	return treeInfo.isBalanced
    #return False

def getTreeInfo(node):
	if node is None:
		return TreeInfo(True,-1)
	leftSubTree=getTreeInfo(node.left)
	rightSubTree=getTreeInfo(node.right)
	isBalanced=(
		leftSubTree.isBalanced
		and rightSubTree.isBalanced 
		and abs(leftSubTree.height-rightSubTree.height)<=1
	)
	height=max(leftSubTree.height,rightSubTree.height)+1
	return TreeInfo(isBalanced,height)

		