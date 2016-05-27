import Point 
import Euclidean 

#Return list of 2 elements - nearest center of point Point from Centers, 
#Euclidean distance between them and index of nearest center
def NearestCenter(Point, Centers):
	minDistance = Euclidean.EuclideanDistance(Point, Centers[0])
	minDistanceIndex = 0
	for i in range(1, len(Centers)):
		currentDistance = Euclidean.EuclideanDistance(Point, Centers[i])
		if currentDistance < minDistance:
			minDistance = currentDistance
			minDistanceIndex = i
	return [Centers[minDistanceIndex], minDistance, minDistanceIndex]


#return min distance of two points in different clusters
def MinDistance(Cluster1, Cluster2):
  minDistance=Euclidean.EuclideanDistance(Cluster1[0], Cluster2[0])
  #print (minDistance)
  
  for i in range (0, len(Cluster1)):
    for j in range (0, len(Cluster2)):
      currentDistance=Euclidean.EuclideanDistance(Cluster1[i], Cluster2[j])
      #print(i, j, currentDistance)
      if(currentDistance < minDistance):
        minDistance=currentDistance
        
  #print(minDistance, Cluster1[i], i, Cluster2[j], j)
  return minDistance      
