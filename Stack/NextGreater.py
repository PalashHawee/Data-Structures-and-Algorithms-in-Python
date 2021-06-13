#Find the next greater element

#Soultion one---> counting forward
#Time and Space O(n) 
def nextGreaterElement(array):
   
	result=[-1]*len(array)
	stack=[]
	for idx in range(2*len(array)):
		circularIdx=idx%len(array)
		#checking if top is less than array cur element
		#len(stack)>0 making sure initiallly stack is not empty
		while len(stack)>0 and array[stack[len(stack)-1]]<array[circularIdx]:
			top=stack.pop()
			result[top]=array[circularIdx]
		stack.append(circularIdx)
	return result	
		
		
		
    return []
#Second solution--> counting from backward  
#Time and Space O(n)  
def nextGreaterElement(array):
   
	result=[-1]*len(array)
	stack=[]
	for idx in range(2*len(array)-1,-1,-1):
		circularIdx=idx%len(array)
		while len(stack)>0:
			if stack[len(stack)-1]<=array[circularIdx]:
				stack.pop()
			else:
				result[circularIdx]=stack[len(stack)-1]
				break
		stack.append(array[circularIdx])
	return result	
    return []