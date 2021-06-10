#Implementing Stack using Array
class StackArray:
	def __init__(self):
		self.data=[]

	def __len__(self):
		return len(self.data)

	def isEmpty(self):
		return len(self.data)==0

	def push(self,e):
		
		self.data.append(e)
		
	def pop(self):
		if self.isEmpty():
			print("Stack is Empty/underflow")
			return
		return self.data.pop()
		
	def top(self):
		if self.isEmpty():
			print("Stack is Empty")
			return
		return self.data[-1] #for printing reverse order								

s=StackArray()
s.push(5)
s.push(1)
s.push(2)
s.push(3)
print(s.data)
print("Length:",len(s))
s.pop()
print(s.data)
print("Length:",len(s))	
print(s.pop())
s.pop()
s.pop()
s.pop()
print(s.isEmpty())	