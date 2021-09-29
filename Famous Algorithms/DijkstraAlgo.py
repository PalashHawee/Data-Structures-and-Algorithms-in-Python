#Implement Dijkstra Algo with a given directed wieghted graph
#Time O(v^2+e) | Space O(v) where v is the no of vertices and
# e no of the edges

def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    numberOfVertices=len(edges)
	minDistances=[float("inf") for _ in range(numberOfVertices)]
	minDistances[start]=0
	visited=set()
	
	while len(visited)!=numberOfVertices:
		vertex, currentMinDistance=getVertexWithMinDistance(minDistances,visited)
		if currentMinDistance==float("inf"):
			break
		visited.add(vertex)
		for edge in edges[vertex]:
			destination, distanceToDestination=edge
			if destination in visited:
				continue
			newPathDistance=currentMinDistance+distanceToDestination
			currentDestinationDistance=minDistances[destination]
			if newPathDistance <currentDestinationDistance:
				minDistances[destination]=newPathDistance
	return list(map(lambda x:-1 if x==float("inf") else x,minDistances))

def getVertexWithMinDistance(distances,visited):
	currentMinDistance=float("inf")
	vertex=-1
	for vertexIdx, distance in enumerate(distances):
		if vertexIdx in visited:
			continue
		if distance <= currentMinDistance:
			vertex=vertexIdx
			currentMinDistance=distance
	return vertex, currentMinDistance		