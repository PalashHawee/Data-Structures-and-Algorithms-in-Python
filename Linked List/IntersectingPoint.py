#Finding Intersecting point in two linked list

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

def IntersectingPoint(head1,head2):
	cur1=head1
	cur2=head2

	if(not cur1 or not cur2):
		return -1
	while (cur1 and cur2 and cur1!=cur2):
		cur1=cur1.next
		cur2=cur2.next

		if(cur1==cur2):
			return cur1.data

		if (not cur1):
			cur1=head2
		if (not cur2):
			cur2=head1
	return cur1.data
		
head1=Node(10)
head2=Node(12)
newNode=Node(2)
head2.next=newNode
newNode=Node(5)
head1.next=newNode
head2.next.next=newNode
newNode=Node(7)
head1.next.next=newNode

head1.next.next.next=None	
point=IntersectingPoint(head1,head2)

print("Intersecting point is: ",point)							