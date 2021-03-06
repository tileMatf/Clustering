import Point
import Print
import FarthestFirstTraversal
import SquaredErrorDistortion
import NearestCenter


#Implement k centers algorithm - select k centers with 
#Farthest first traversal heuristic and arrange point in
#cluster whose center is nearest 
def k_Center(Points):
	
	k = Input.EnterNumberOfCluster(Points);
	Centers = FarthestFirstTraversal.FarthestFirstTraversal(Points, k)
	n = len(Points)

	Clusters = []	
	for i in range(0, k):
		Clusters.append([])

	for i in range(0, n):
		nearestCenter = NearestCenter.NearestCenter(Points[i], Centers)
		for j in range(0, len(Centers)):
			if FarthestFirstTraversal.EqualPoints(nearestCenter[0], Centers[j]):
				Clusters[j].append(Points[i])
	return Clusters

#Example
a = Point.Point([1,6])
b = Point.Point([1,3])
c = Point.Point([3,4])
d = Point.Point([5,6])
e = Point.Point([5,2])
f = Point.Point([7,1])
g = Point.Point([8,7])
h = Point.Point([10,3])

Points = [a, b, c, d,e,f,g,h]
Clusters = k_Center(Points, 3)

Print.PrintClusters(Clusters)