#Counting Nodes and Sum of all nodes in a Singly Linked List
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

#creating LinkedList 		
class LinkedList:

	#initialising head  to None
	def __init__(self):
		self.head=None
		

	#inserting elements func
	def push(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node

	#counting nodes
	def count(self):
		temp=self.head #pointer
		c=0
		while(temp):
			c+=1
			temp=temp.next
		return c
	
	#Summation of all elements
	def Add(self):
		ptr=self.head
		sum=0
		while(ptr!=None):
			sum=sum+ptr.data
			ptr=ptr.next
		return sum
		

	
LList=LinkedList()
LList.push(4)
LList.push(5)
LList.push(1)

print("No of elements is: ",LList.count())
print("Sum of all elements is: ", LList.Add())	

#Time O(N) max
#Min time O(1)					



		