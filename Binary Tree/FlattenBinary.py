# Write a function to return in a Binary Tree, flattens it and return its leftmost node

#Time O(N) and space O(d) where d is the depth of the tree
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    # Write your code here.
	leftMost,_=flattenTree(root)
	return leftMost
def flattenTree(node):
	if node.left is None:
		leftMost=node
	else:
		leftSubTreeLeftMost,leftSubTreeRightMost=flattenTree(node.left)
		connectNodes(leftSubTreeRightMost,node)
		leftMost=leftSubTreeLeftMost
	if node.right is None:
		rightMost=node
	else:
		rightSubTreeLeftMost,rightSubTreeRightMost=flattenTree(node.right)
		connectNodes(node,rightSubTreeLeftMost)
		rightMost=rightSubTreeRightMost
	return [leftMost,rightMost]
def connectNodes(left,right):
	left.right=right
	right.left=left
    
