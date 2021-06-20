#Inorder Iterative traversal using stack
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def InOrder(root):
	current=root
	stack=[]

	while True:
		if current is not None:
			stack.append(current)
			current=current.left
		elif(stack):
			current=stack.pop()	
			print(current.data,end=' ')
			current=current.right

		else:
			break
	print()
		
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(5)
root.left.right=Node(7)
root.right.left=Node(10)
print("Inorder Traversed :")
InOrder(root)					