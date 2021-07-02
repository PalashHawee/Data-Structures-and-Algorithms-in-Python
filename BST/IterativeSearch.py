#Creating BST using Linked representation
class Node:
	__slots__='data','left','right'
	def __init__(self,data,left=None,right=None):
		self.data=data
		self.left=left
		self.right=right

class BinarySearchTree:
	#Creating root node
	def __init__(self):
		self.root=None

	#Inserting Algorithm
	#Time O(n) and searching O(logn)
	'''def Insert(self,pointer,key):
		temp=None
		while pointer:
			temp=pointer
			if key==pointer.data:
				return
			elif key<pointer.data:
				pointer=pointer.left
			elif key>pointer.data:
				pointer=pointer.right
		newNode=Node(key)
		if self.root:
			if key<temp.data:
				temp.left=newNode
			else:
				temp.right=newNode
		else:
			self.root=newNode'''

		#Recursive Insertion
	def ReInsert(self,pointer,key):
		if pointer:
			if key<pointer.data:
				pointer.left=self.ReInsert(pointer.left,key)
			elif key>pointer.data:
				pointer.right=self.ReInsert(pointer.right,key)
		else:
			newNode=Node(key)
			pointer=newNode
			return pointer	

	#Iterative search algorithm takes O(h) time
	#Where h is the height of the tree
	def Isearch(self,key):
		pointer=self.root
		while pointer:
			if key==pointer.data:
				return pointer
			elif key<pointer.data:
				pointer=pointer.left
			else:
				pointer=pointer.right
			return None	#if key is not found

	#Recursive Search algo takes O(h) time also like Iterative search above
	def reSearch(self,p,key):
		if p==None:
			return None	
		if key==p.data:
			return p	
		elif key<p.data:
			return self.reSearch(p.left,key)
		else:
			return self.reSearch(p.right,key)			


	#Inorder Traversal for displaying Tree
	def Inorder(self,pointer):
		if pointer:
			self.Inorder(pointer.left)
			print(pointer.data,end=' ')
			self.Inorder(pointer.right)

B=BinarySearchTree()
B.root=B.ReInsert(B.root,50)
B.ReInsert(B.root,40)
B.ReInsert(B.root,100)
B.ReInsert(B.root,20)
B.ReInsert(B.root,30)
B.Inorder(B.root)	
print()
print(B.reSearch(B.root,50))														