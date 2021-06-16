#Implementing Double Ended Queue using Array
#DEQueue doesn't necessarily support FIFO logic
#Both Rear and Front can be used for insertion and deletion
class DEQueueArray:
	def __init__(self):
		self.data=[]
	def __len__(self):
		return len(self.data)
	def isEmpty(self):
		return len(self.data)==0
	def AddFirst(self,e):
		return self.data.insert(0,e)
	def AddLast(self,e):
		return self.data.append(e)
	def RemoveFirst(self):
		if self.isEmpty():
			print("DEQueue is Empty")
			return
		return self.data.pop(0)
	def RemoveLast(self):
		if self.isEmpty():
			print("DEQueue is Empty")
			return
		return self.data.pop()
	def DisplayFirst(self):
		if self.isEmpty():
			print("DEQueue is Empty")
			return
		return self.data[0]
	def DisplayLast(self):
		if self.isEmpty():
			print("DEQueue is Empty")
			return
		return self.data[-1]
		
d=DEQueueArray()
d.AddFirst(2)
d.AddFirst(3)
d.AddFirst(4)
d.AddLast(10)
d.AddLast(15)
print(d.data)
print("lenght :",len(d))
print(d.RemoveFirst())
print(d.RemoveLast())
print(d.data)
print("length :",len(d))
print("First Element :",d.DisplayFirst())	
print("Last Element :",d.DisplayLast())												