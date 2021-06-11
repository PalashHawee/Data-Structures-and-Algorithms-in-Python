#Finding Min Max with Time O(1) and extra space O(1) using Array

class MinMaxStack:
	
	def __init__(self):
		self.minMaxStack=[]
		self.stack=[]

    def peek(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        
        self.minMaxStack.pop()
		return self.stack.pop()

    def push(self, number):
        
        newMinMax={"Min":number,"Max":number}
		if (len(self.minMaxStack)):
			lastMinMax=self.minMaxStack[len(self.minMaxStack)-1]
			newMinMax["Min"]=min(lastMinMax["Min"],number)
			newMinMax["Max"]=max(lastMinMax["Max"],number)
		self.minMaxStack.append(newMinMax)
		self.stack.append(number)

    def getMin(self):
        
        return self.minMaxStack[len(self.minMaxStack)-1]["Min"]

    def getMax(self):
        
        return self.minMaxStack[len(self.minMaxStack)-1]["Max"]

s=MinMaxStack()
s.push(5)
s.push(7)
s.push(10)
s.push(11)
s.push(2)        

