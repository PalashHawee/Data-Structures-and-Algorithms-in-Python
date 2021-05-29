#Deleting First node of singly linked list

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
	L.Display()
	print("Size is :",len(L))
	L.DeleteFirst()
	
	L.Display()	
	print("Size is: ",len(L))					

