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

	#Recursively counting nodes
	def Rcount(self,node):
		if(not node):
			return 0
		else:
			return self.Rcount(node.next)+1	
	#A wrapper over Rcount
	def count(self):
		return self.Rcount(self.head)		
	
	#Recursively Summation of all elements
	def RAdd(self,node):
		if (not node):
			return 0
		else:
			return self.RAdd(node.next)+node.data

	def Add(self):
		return self.RAdd(self.head)				
			
			
LList=LinkedList()
LList.push(4)
LList.push(5)
LList.push(1)

print("No of elements is: ",LList.count())
print("Sum of all elements is: ", LList.Add())	

#Time O(N) max
#Min time O(1)					



		