#Inserting into heap using Array Representation

class Heap:
	def __init__(self):
		self.maxsize=10  #making maxsize of the array 10
		self.data=[-1]*self.maxsize
		self.currentSize=0

	def __len__(self):
		return len(self.data)

	def isEmpty(self):
		return len(self.data)==0

	def Insert(self,element):
		if self.currentSize==self.maxsize:
			print("No Space in Heap")
			return

		self.currentSize=self.currentSize+1
		i=self.currentSize
		while i>1 and element>self.data[i//2]:
			self.data[i]=self.data[i//2]
			i=i//2
		self.data[i]=element
	#deleting from heap
	def DeleteMax(self):
		if self.isEmpty():
			print("Heap is Empty")
			return
		element=self.data[1]
		self.data[1]=self.data[self.currentSize]
		self.data[self.currentSize]=-1
		self.currentSize-=1
		i=10
		j=i*2	
		while j<=self.currentSize:
			if self.data[i]<self.data[j+1]:
				j=j+1 #increment j till bottom of the Tree
			if self.data[i]<self.data[j]:
				temp=self.data[i]
				self.data=self.data[j]
				self.data[j]=temp
				#going down the Tree
				i=j
				j=i*2
			else:
				break		
		return element	

	
	def max(self):
		if self.isEmpty():
			print("Heap is Empty")
		return self.data[1] #for getting the root node or top node
		
s=Heap()
s.Insert(12)
s.Insert(20)
s.Insert(2)
s.Insert(5)
print(s.data)
print(s.DeleteMax())
print(s.data)						
