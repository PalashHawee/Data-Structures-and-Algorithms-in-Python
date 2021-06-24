#Inverting Binary Tree Recursively and Iteratively

#Iteratively
#Time O(n) and space(n) where n is the number of nodes
def invertBinaryTree(tree):
    
    queue=[tree]
	while len(queue):
		current=queue.pop(0)
		if current is None:
			continue
		swapLeftAndRight(current)
		queue.append(current.left)
		queue.append(current.right)
def swapLeftAndRight(tree):
	tree.left,tree.right=tree.right,tree.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Recursive way
#Time O(n) and space O(d or h) where d/h is the depth and height of the tree        
def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
		return
	swapLeftAndRight(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
def swapLeftAndRight(tree):
	tree.left,tree.right=tree.right,tree.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None