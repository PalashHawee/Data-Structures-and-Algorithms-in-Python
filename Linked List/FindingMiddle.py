#Finding Middle Node in the Linked List

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
	#Inserting at given position
	#Time max O(N) min O(1)
	def InsertAny(self,e,position):
		newest=Node(e,None,None)
		p=self.head
		i=1	
		while i<position-1:
			p=p.next
			i+=1

		newest.next=p.next
		newest.prev=p	
		if p.next: #checking if p.next is available special case
			p.next.prev=newest
		p.next=newest
		self.size+=1

	#Deleting First Node of Doubly LL
	#Time O(1)
	def DeleteFirst(self):
		if self.isEmpty():
			print("List is empty")
			return
		p=self.head.data
		self.head=self.head.next
		#checking if it's pointing to some node previouly
		if self.head:
			self.head.prev=None
		self.size-=1	
		#againg checking if after deleting list is empty
		#then head and tail will be null so now making tail null
		if self.isEmpty():
			self.tail=None
		return p

	#Deleting Last Node
	def DeleteLast(self):
		if self.isEmpty():	
			print("List is empty")
			return
		p=self.tail.data
		self.tail=self.tail.prev
		self.tail.next=None
		self.size-=1
		return p

	#Deleting at any given position including last node
	def DeleteAny(self,position):
		if self.isEmpty():
			print("List is empty")
			return
		p=self.head
		i=1
		while i<position-1:
			p=p.next
			i+=1
		p.prev.next=p.next
		#checking p.next is available or p is the last node
		#we r deleting	
		if p.next:
			p.next.prev=p.prev
		self.size-=1
		return p
	#finding middle node using two pointers
	#one pointer moves 1 node other moves 2 nodes at a time	
	def Middle_Node(self):
		p=self.head
		q=self.head
		if self.head is not None:
			while(q is not None and q.next is not None):
				q=q.next.next
				p=p.next
			print("The Middle element is:",p.data)	
						
		
D=DoublyLinkedList()
D.push(5)
D.push(8)
D.push(7)
D.push(10)
D.Display()
print("Length is: ",len(D))	
#D.DisplayRev()
D.Middle_Node()
D.Display()
#print("Middle element is: ",ele)

#D.DisplayRev()
