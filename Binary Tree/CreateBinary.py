#Creating binary tree using linked representation
class Node:
	__slots__='data','left','right'
	def __init__(self,data,left=None,right=None):
		self.data=data
		self.left=left
		self.right=right

class BinaryTree:
	def __init__(self):
		self.root=None

	def CreateTree(self,e,left,right):
		self.root=Node(e,left.root,right.root)

	def Inorder(self,troot):
		if troot:
			self.Inorder(troot.left)
			print(troot.data,end=' ')
			self.Inorder(troot.right)

	def PreOrder(self,troot):
		if troot:
			print(troot.data,end=' ')
			self.PreOrder(troot.left)
			self.PreOrder(troot.right)

	def PostOrder(self,troot):
		if troot:
			self.PostOrder(troot.left)
			self.PostOrder(troot.right)
			print(troot.data,end=' ')


x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
a = BinaryTree()
x.CreateTree(40,a,a)
y.CreateTree(60,a,a)
z.CreateTree(20,x,a)
r.CreateTree(50,a,y)
s.CreateTree(30,r,a)
t.CreateTree(10,z,s)
print('Inorder Traversal')
t.Inorder(t.root)
print()
print('Preorder Traversal')
t.PreOrder(t.root)
print()
print('Postorder Traversal')
t.PostOrder(t.root)

