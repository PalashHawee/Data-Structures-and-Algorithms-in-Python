#Inserting before first node in Doubly Linked List

class Node:
	__slots__='data','next','prev'
	def __init__(self,data,next,prev):
		self.data=data
		self.next=next
		self.prev=prev

class DoublyLinkedList:
	def __init__(self):
		self.head=None
		self.tail=None
		self.size=0
	def __len__(self):
		return self.size

	def isEmpty(self):
		return self.size==0
	#Adding elements
	#Time O(1)	
	def push(self,e):
		newest=Node(e,None,None)

		if self.isEmpty():
			self.head=newest
			self.tail=newest					
		else:
			self.tail.next=newest
			newest.prev=self.tail
			self.tail=newest
		self.size+=1	

	def Display(self):
		p=self.head

		while p:
			print(p.data,end='->')
			p=p.next

		print()

	#To display reversely since it has previous address also in Doubly LL
	def DisplayRev(self):
		p=self.tail
		while p:
			print(p.data,end='<-')
			p=p.prev
		print()	

	#Inserting before 1st node takes O(1) time
	def InsertFirst(self,e):
		newest=Node(e,None,None)
		if self.isEmpty():
			self.head=newest
			self.tail=newest

		else:
			newest.next=self.head
			self.head.prev=newest
			self.head=newest
		self.size+=1				
		
D=DoublyLinkedList()
D.push(5)
D.push(8)
D.push(7)
D.push(10)
D.Display()
print("Length is: ",len(D))	
D.DisplayRev()
D.InsertFirst(20)
D.Display()
print("Length is: ",len(D))	
D.DisplayRev()
