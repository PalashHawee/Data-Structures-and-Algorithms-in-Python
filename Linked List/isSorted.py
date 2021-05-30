#Checking if singly LL is sorted

class Node:
	#__slots__='_elem','_next' #reducing memory creating dictionary for lots of objects
	def __init__(self,data,next):
		self.data=data
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

	#searching algorithm
	def LSearch(self,key):
			p=self.head
			index=0
			while p:
				if key==p.data:
					return index
				p=p.next
				index+=1
			return -1
	#Removing first node algo
	#time O(1)
	def DeleteFirst(self):
		if self.isEmpty():
			print("List is Empty ")
			return
		e=self.head.data
		self.head=self.head.next
		self.size-=1

		if self.isEmpty():
			self.tail=None

	#Deleting Last Node
	#Time O(N) for the traversing in while loop
	def RemeoveLast(self):
		if self.isEmpty():
			print("List is Empty")
			return
		p=self.head
		i=1
		while i<len(self)-1:
			p=p.next
			i+=1
		self.tail=p
		p=p.next
		e=p.data
		self.tail=None
		self.size-=1
		return e	
	#Deleting at Given position
	#Time O(N)	
	def DeleteAny(self,position):
		p=self.head
		i=1

		while i<position-1:
			p=p.next
			i+=1
		e=p.next.data
		p.next=p.next.next
		self.size-=1
		return e
	#checking if List is sorted
	#Min time O(1) and Max time O(N)
	def isSorted(self):
		x=-65536
		p=self.head
		while p:
			if(p.data<x):
				return False
			x=p.data
			p=p.next
		return True								
					
	
	def Display(self):
		p=self.head
		while p:
			print(p.data,end='->')
			p=p.next
		print(None)	

if __name__=='__main__':
	L=LinkedList()
	L.AddLast(12)
	L.AddLast(8)
	L.AddLast(10)
	L.AddLast(2)
	L.AddLast(100)
	L.Display()
	#print("Size is :",len(L))
	#ele=L.DeleteAny(5)
	#print(L.isSorted())
	if(L.isSorted()):
		print("Yes it's sorted")
	else:
		print("Not sorted")	
	
	#L.Display()	
	#print("Size is: ",len(L))
	#print("Element Removed is: ",ele)					

