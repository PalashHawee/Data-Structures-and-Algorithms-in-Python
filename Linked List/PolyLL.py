#Polynomial Representation using singly Linked List
class Node:
	def __init__(self,coeff,expo):
		self.coeff=coeff
		self.expo=expo
		self.next=None

class polynomial:
	def __init__(self):
		self.head=None

	def CreateNode(self):
		coeff=int(input("Enter Coefficient"))
		expo=int(input("Enter Exponent"))
		newNode=Node(coeff,expo)
		return newNode

	def PolyList(self):
		while True:
			print("Create a polynomial?")
			answer=input()
			if answer=='N':
				break
			newNode=self.CreateNode()
			if self.head==None:
				self.head=newNode
			else:
				p=self.head
				while p:
					p=p.next
				p.next=newNode
				
	def Display(self):
		p=self.head
		while p:
			print("%dx^%d+"%(p.coeff,p.expo),end='')
			p=p.next
		#print("%d"%(p.data))	


a=polynomial()
a.PolyList()
a.Display()													