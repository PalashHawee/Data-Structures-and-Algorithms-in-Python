#Implementing Queue using Array
#Time complexity is O(1) and space is O(1)
class QueuesArray:
	def __init__(self):
		self.data=[] #for queue
	def __len__(self):
		return len(self.data)
	def isEmpty(self):
		return len(self.data)==0

	def enqueue(self,e):
		self.data.append(e)

	def dequeue(self):
		#first checking if queue is empty or not
		if self.isEmpty():
			print("Queue is Empty")
			return
		return self.data.pop(0)
	def first(self):
		#checking first if queue is empty
		if self.isEmpty():
			print("Queue is Empty")
			return
		return self.data[0]
		
Q=QueuesArray()
Q.enqueue(12)
Q.enqueue(20)
Q.enqueue(30)
print(Q.data)
print("length:",len(Q))
print(Q.first())
Q.dequeue()
print(Q.data)
print("length:",len(Q))
		