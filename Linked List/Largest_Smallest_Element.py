#Finding Largest and Smallest number in the linked list

class Node:
	def __init__(self):
		self.data=None
		self.next=None

head=None
def LargestNum(head): 
	max=-32767
	while head:
		if(max<head.data):
			max=head.data
		head=head.next

	return max

def SmallestNum(head): 
	min=32767
	while head:
		if(min>head.data):
			min=head.data
		head=head.next

	return min

	
#Adding Numbers
def push(data):
	global head
	newNode=Node()
	newNode.data=data
	newNode.next=(head)
	(head)=newNode

def DisplayLL(head):
	while(head!=None):
		print(head.data,end='->')
		head=head.next

	print('None')
	

'''push(5)	
push(10)	
push(1)	
push(25)	
push(26)'''
push(int(input()))
push(int(input()))
push(int(input()))
push(int(input()))
DisplayLL(head)	
print("Largest Number is: ",LargestNum(head))
print("Smallest Number is: ",SmallestNum(head))					

