#Preorder Iterative traversal using stack
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def PreOrder(root):
	current=root
	stack=[]

	while True:
		if current is not None:
			print(current.data,end=' ')
			stack.append(current)
			current=current.left
		elif(stack):
			current=stack.pop()	
			
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
print("Preorder Traversed :")
PreOrder(root)					