class Node:
	def __init__(self,element,next):
		self.element=element
		self.next=next

n1=Node(7,None)
n2=Node(9,None)
n1.next=n2
#print(n1.next)

print(n1.element)		