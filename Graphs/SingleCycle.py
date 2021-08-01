#Algorithm to check the Single Cycle

#Time O(N) where  N is the number of inputs in the array
#Space O(1) since it doesn't use extra space or array

def hasSingleCycle(array):
    # Write your code here.
    numElementsVisited=0
	currentIdx=0
	while numElementsVisited<len(array):
		if numElementsVisited>0 and currentIdx==0:
			return False
		numElementsVisited+=1
		currentIdx=getNextIdx(currentIdx,array)
	return currentIdx==0
def getNextIdx(currentIdx,array):
	jump=array[currentIdx]
	nextIdx=(currentIdx+jump)%len(array)
	return nextIdx if nextIdx>=0 else nextIdx+len(array)
