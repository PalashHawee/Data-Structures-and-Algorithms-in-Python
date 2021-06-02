#Displaying Cicular linked list

class Node:
	#__slots__='_elem','_next' #reducing memory creating dictionary for lots of objects
	def __init__(self,data,next):
		self.data=data
		self.next=next

class CircularLinkedList:
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
	def AddLast(self,e):
		newest=Node(e,None)
		if self.isEmpty():
			newest.next=newest
			self.head=newest
		else:
			newest.next=self.tail.next	
			self.tail.next=newest
		self.tail=newest
		self.size+=1

	#Displaying	Circular LL
	def Display(self):
		p=self.head
		i=0
		while (i<len(self)):
			print(p.data,end='->')
			p=p.next
			i+=1
		print()
		
Cir=CircularLinkedList()
Cir.AddLast(5)
Cir.AddLast(10)
Cir.AddLast(20)
Cir.AddLast(15)
Cir.Display()
print("size: ",len(Cir))				