'''Creating and Displaying Linked List'''

class Node:
	#__slots__='_elem','_next' #reducing memory creating dictionary for lots of objects
	def __init__(self,element,next):
		self.element=element
		self.next=next

class LinkedList:
	def __init__(self):
		self.head=None
		self.tail=None
		self.size=0
	#checking length
	
	def __len__(self):
		return self.size

	#checking func
	
	def isEmpty(self):
		return self.size==0

	#adding elem func
	
	def AddLast(self,elem):
		newest=Node(elem,None)

		if self.isEmpty():
			self.head=newest

		else:
			self.tail.next=newest
		self.tail=newest
		self.size+=1

	def Display(self):
		p=self.head

		while p:
			print(p.element,end='->')
			p=p.next
		print()	

L=LinkedList()
L.AddLast(12)
L.AddLast(8)
L.AddLast(10)
L.Display()							

