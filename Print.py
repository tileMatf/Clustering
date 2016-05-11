import Point

#Print list of points in readable form	
def PrintPoints(Points):	
	print()
	for i in range(0, len(Points)):
		if i != len(Points) - 1:
			print(Points[i].coord, end=", ")
		else:
			print(Points[i].coord)
			print()
			
#Print clusters in readable form
def PrintClusters(Clusters):
	for i in range(0, len(Clusters)):
		print(str(i+1) + ". cluster")
		PrintPoints(Clusters[i])