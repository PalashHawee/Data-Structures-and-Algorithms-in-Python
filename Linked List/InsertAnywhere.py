'''Inserting Element at a Given position'''

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
	
	def Push(self,elem):
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

	def AddFirst(self,t):
			newest=Node(t,None)
			if self.isEmpty():
				self.head=newest
				self.tail=newest
			#if it's not empty then add at the beginning of the list
			#and assign the next pointer to head in the existing list	
			else:
				newest.next=self.head
				self.head=newest
			self.size+=1
	#Inserting anywhere algo
	#Time O(n) for while loop
	def InsertAny(self,t,position):
		newest=Node(t,None)
		p=self.head
		i=1
		while i<position-1:
			p=p.next
			i+=1
		newest.next=p.next
		p.next=newest
		self.size+=1	

		
	def Display(self):
		p=self.head
		while p:
			print(p.data,end='->')
			p=p.next
		print(None)	

if __name__=='__main__':
	L=LinkedList()
	L.Push(12)
	L.Push(8)
	L.Push(10)
	L.Display()
	L.InsertAny(20,3)
	L.Display()
	#L.AddFirst(20)
	print("Size :",len(L))
	
							

