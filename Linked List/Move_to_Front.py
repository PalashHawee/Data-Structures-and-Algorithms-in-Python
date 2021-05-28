#Move to front method
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None

	def push(self,data):
		new_Node=Node(data)
		new_Node.next=self.head
		self.head=new_Node

	def PrintList(self):
		tmp=self.head
		while tmp:
			print(tmp.data,end='->')

			tmp=tmp.next
		print('None')
		
	#moving to front algo
	def MovingFront(self,key):
		tmp=self.head
		q=None
		while tmp:
			if(key==tmp.data):
				q.next=tmp.next
				tmp.next=self.head
			q=tmp
			tmp=tmp.next	

	'''def MovingFront(self):
		tmp=self.head
		sec_last=None
		if not tmp or tmp.next:
			return
		while tmp and tmp.next:
			sec_last=tmp
			tmp=tmp.next
		sec_last.next=None
		tmp.next=self.head
		self.head=tmp'''


Li=LinkedList()
Li.push(5)
Li.push(10)
Li.push(2)
Li.push(1)
Li.push(8)
Li.PrintList()
Li.MovingFront(10)									