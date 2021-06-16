#Implementing Queue using Linked List
class Node:
	__slots__='data','next'
	def __init__(self,data,next):
		self.data=data
		self.next=next
class QueueLinked:
	def __init__(self):
		self.front=None
		self.rear=None
		self.size=0
	def __len__(self):
		return self.size
	def isEmpty(self):
		return self.size==0

	def enqueue(self,e):
		newest=Node(e,None)
		if self.isEmpty():
			self.front=newest
		else:
			self.rear.next=newest
		self.rear=newest
		self.size+=1

	def dequeue(self):
		if self.isEmpty():
			print("Queue is Empty")
			return
		p=self.front.data
		self.front=self.front.next
		self.size-=1
		if self.isEmpty():
			self.rear=None
		return p	

	def first(self):
		if self.isEmpty():
			print("Queue is Empty")
			return
		return self.front.data
		
	def display(self):
		p=self.front
		while p:
			print(p.data,end=" ->")
			p=p.next
		print()
		


q=QueueLinked()
q.enqueue(5)
q.enqueue(2)
q.enqueue(6)
q.enqueue(8)
q.enqueue(10)
q.display()
print("Length :",len(q))
q.dequeue()
q.first()
q.display()
print("Length :",len(q))													
