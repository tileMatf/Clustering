import MinDistance
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
    print (i, ":", Clusters[i])
   
  
  while(len(Clusters)>1):
    minDist=MinDistance.MinDistance(Clusters[0], Clusters[1])
    ind1=0
    ind2=1
    for i in range (0, len(Clusters)):
      for j in range (i+1, len(Clusters)):
        minDistTemp=MinDistance.MinDistance(Clusters[i], Clusters[j])
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
      print (i, ":", Clusters[i])
  

w, h = 5, 3
matrix = [[0 for x in range(w)] for y in range(h)] 

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

points=[ d.coord, q.coord, w.coord, a.coord, b.coord, c.coord]
  
HierarhicalClustering(matrix, points )  
