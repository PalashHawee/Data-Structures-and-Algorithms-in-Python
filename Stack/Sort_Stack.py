#Write a function that takes an array of integers representing a stack
#recursively sort the stack in place(without accessing their indices)
#Time O(n^2) and space O(n)
def sortStack(stack):
    
	if len(stack)==0:
		return stack
	top=stack.pop()
	sortStack(stack)
	insertInSortedPosition(stack,top)
	return stack
def insertInSortedPosition(stack,value):
	if len(stack)==0 or stack[len(stack)-1]<=value:
		stack.append(value)
		return
	top=stack.pop()
	insertInSortedPosition(stack,value)
	stack.append(top)
    return []