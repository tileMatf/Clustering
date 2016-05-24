import Point 
import math

def EuclideanDistance(Point1, Point2):
	distance = 0
	n = Point1
	m = Point2
	#print n, len(n)
	
	for i in range(0, len(n)):
		distance += pow((n[i]-m[i]), 2)
	distance = round(math.sqrt(distance),2)
	#print distance
	return distance


#Return list of 2 elements - nearest points of two Clusters 
#and Euclidean distance between them
def MinDistance(Cluster1, Cluster2):
  minDistance=EuclideanDistance(Cluster1[0], Cluster2[0])
  
  for i in range (0, len(Cluster1)):
    for j in range (0, len(Cluster2)):
      currentDistance=EuclideanDistance(Cluster1[i], Cluster2[j])
      #print(i, j, currentDistance)
      if(currentDistance < minDistance):
        minDistance=currentDistance
        
  #print(minDistance, Cluster1[i], i, Cluster2[j], j)
  return minDistance      
      
  
a = Point.Point([1,2])
b = Point.Point([6,8])
c = Point.Point([3,4])
d = Point.Point([5,6])
e = Point.Point([5,2])
f = Point.Point([4,3])
g = Point.Point([8,7])
h = Point.Point([9,3])
q = Point.Point([1,3])
w = Point.Point([2,6])
r = Point.Point([3,8])
p = Point.Point([3,1])

#print (EuclideanDistance(a.coord, b.coord))


#Cluster1=[ d.coord, q.coord, w.coord, a.coord, b.coord, c.coord]
#print(Cluster1)
#Cluster2 = [g.coord,h.coord, r.coord, p.coord, e.coord,f.coord]
#print(Cluster2)
#MinDistance(Cluster1, Cluster2)
