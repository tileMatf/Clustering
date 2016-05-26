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
		print("--------------------------------")
		
		
def PrintClustersThrowVector(Data, HiddenVector, k):
	
	for i in range(0, k):
		print()
		print(str(i+1) + ". cluster")
		for j in range(0, len(HiddenVector)):
			if HiddenVector[j] == i:
				print(Data[j].coord, end="")
				if j != len(HiddenVector)-1:
					print(", ", end="")
		print()
		print("--------------------------------")