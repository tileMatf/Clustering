import NearestCenter
import Point

def HierarhicalClustering(matrixD, points):
  
	n=len(points)
	Clusters=[]
	for i in range(0, n):
		Clusters.append([])
	# print Clusters
	
	print ("Clusters:")
	for i in range (0, n):
		Clusters[i].append(points[i])
	
	for i in range (0, n):
		for j in range (0, len(Clusters[i])):
			print (i, ":", Clusters[i][j].coord)
   
  
	while(len(Clusters)>1):
		minDist=NearestCenter.MinDistance(Clusters[0], Clusters[1])
		ind1=0
		ind2=1
		
		for i in range (0, len(Clusters)):
			for j in range (i+1, len(Clusters)):
				minDistTemp=NearestCenter.MinDistance(Clusters[i], Clusters[j])
				#print minDistTemp, i, j
				if(minDistTemp<minDist):
					minDist=minDistTemp
					ind1=i
					ind2=j
      
		print ("merge",  ind1, "and", ind2, "minDistance =", minDist)
		for i in range(0, len(Clusters[ind2])):
			Clusters[ind1].append(Clusters[ind2][i])
		del Clusters[ind2]  
		n=n-1
			
		print ("CLusters:")
		for i in range (0, n):
			print (i, ":", end=" ")
			for j in range (0, len(Clusters[i])):
				if j !=len(Clusters[i])-1: 
					print(Clusters[i][j].coord, end=", ")
				else:
					print(Clusters[i][j].coord)
					print()
  

w, h = 5, 3
matrix = [[0 for x in range(w)] for y in range(h)] 

a = Point.Point([1,2, 3])
b = Point.Point([6,8, 4])
c = Point.Point([3,4, 4])
d = Point.Point([5,6, 4])
e = Point.Point([5,2, 4])
f = Point.Point([4,3, 4])
g = Point.Point([8,7, 3])
h = Point.Point([9,3, 3])
q = Point.Point([1,3, 3])
w = Point.Point([2,6, 3])
r = Point.Point([3,8, 3])
p = Point.Point([3,1,3])

points=[ d, q, w, a, b, c]
  
HierarhicalClustering(matrix, points )  
