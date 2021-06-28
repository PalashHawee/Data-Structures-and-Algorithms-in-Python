#Finding Successor in a Binary Tree
#Brute Force/Simple Approach
#Time O(n) where n is the number of nodes and Space O(n)
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
	inOrderTraversal=getInorderTraversal(tree)
	for idx,currentNode in enumerate(inOrderTraversal):
		if currentNode!=node:
			continue
		if idx==len(inOrderTraversal)-1:
			return None
		return inOrderTraversal[idx+1]
			
	
  
def getInorderTraversal(node,order=[]):
	if node is None:
		return order
	getInorderTraversal(node.left,order)
	order.append(node)
	getInorderTraversal(node.right,order)
	return order
#Optimal Approach
#Time O(h) where h is the height of the tree and space O(1)
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    if node.right is not None:
		return getLeftmostChild(node.right)
	return getRightmostChild(node)
def getLeftmostChild(node):
	curNode=node
	while curNode.left:
		curNode=curNode.left
	return curNode
def getRightmostChild(node):
	curNode=node
	while curNode.parent is not None and curNode.parent.right==curNode:
		curNode=curNode.parent
		
	return curNode.parent	