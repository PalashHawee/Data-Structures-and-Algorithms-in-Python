#Largest Rectangle Under Skyline
#The algorithm below takes O(n) time and space

def largestRectangleUnderSkyline(buildings):
    # Write your code here.
	pillarIndices=[]
	maxArea=0
	for pointer,height in enumerate(buildings+[0]):
		while len(pillarIndices)!=0 and buildings[pillarIndices[len(pillarIndices)-1]]>=height:
			pillarHeight=buildings[pillarIndices.pop()]
			width=pointer if len(pillarIndices)==0 else pointer-pillarIndices[len(pillarIndices)-1]-1
			maxArea=max(width*pillarHeight,maxArea)
		pillarIndices.append(pointer)
	return maxArea	
    return 0