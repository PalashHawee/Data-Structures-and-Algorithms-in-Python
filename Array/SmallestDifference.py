#Time O(nlogn+mlogm) where n is the length of first array and
# m is the length of second array
# Space O(1) since not using any extra space

def smallestDifference(arrayOne, arrayTwo):
   
    arrayOne.sort()
	arrayTwo.sort()
	idxOne=0
	idxTwo=0
	smallest=float("inf")
	current=float("inf")
	smallestPair=[]
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum=arrayOne[idxOne]
		secondNum=arrayTwo[idxTwo]
		if firstNum < secondNum:
			current=secondNum-firstNum
			idxOne+=1
		elif secondNum < firstNum:
			current=firstNum-secondNum
			idxTwo+=1
		else:
			return [firstNum, secondNum]
		if smallest > current:
			smallest=current
			smallestPair=[firstNum, secondNum]
	return smallestPair		
			
