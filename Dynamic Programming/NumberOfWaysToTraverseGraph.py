#Number of ways to traverse graph
#Time O(n*m)| Space O(n*m) 
#Where n is the width and m is the height of the graph

def numberOfWaysToTraverseGraph(width, height):
    
    numberOfWays=[[0 for _ in range(width+1)] for _ in range(height+1)]
	for widthIdx in range(1,width+1):
		for heightIdx in range(1, height+1):
			if widthIdx==1 or heightIdx==1:
				numberOfWays[heightIdx][widthIdx]=1
			else:
				waysLeft=numberOfWays[heightIdx][widthIdx-1]
				waysUp=numberOfWays[heightIdx-1][widthIdx]
				numberOfWays[heightIdx][widthIdx]=waysLeft+waysUp
	return numberOfWays[heightIdx][widthIdx]	

#Recursive Solution
# Time O(2^(n+m)) | Sapce O(n+m)
def numberOfWaysToTraverseGraph(width, height):
   
    if width==1 or height==1:
		return 1
	return numberOfWaysToTraverseGraph(width-1,height)+numberOfWaysToTraverseGraph(width,height-1)

				
