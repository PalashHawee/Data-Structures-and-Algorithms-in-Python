#Given an Array of buildings and the direction of the buildings face
#return the indices of the buildings that can see the sunset

#Time and Space Complexity O(N)
def sunsetViews(buildings, direction):
    # Write your code here.
	candidateBuildings=[]
	startIdx=0 if direction == "EAST" else len(buildings)-1
	step=1 if direction =="EAST" else -1
	
	idx=startIdx
	while idx>=0 and idx<len(buildings):
		buildingHeight=buildings[idx]
		while len(stackBuildings)>0 and buildings[candidateBuildings[-1]] <=buildingHeight:
			candidateBuildings.pop()
		candidatebuildings.append(idx)	
		Idx+=step
		
	if direction=="WEST":
		return candidateBuildings[::-1]
	return candidateBuildings
    return []
