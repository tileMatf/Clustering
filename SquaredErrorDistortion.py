import Point
import NearestCenter
import math

def Distortion(Points, Centers):
	sum = 0
	n = len(Points)
	for i in range(0, n):
		nearestCenter = NearestCenter.NearestCenter(Points[i], Centers)
		sum += pow(nearestCenter[1], 2)
	return sum/n	

	
A = Point.Point([1,6])
B = Point.Point([5,6])
C = Point.Point([3,4])
D = Point.Point([1,3])
G = Point.Point([8,7])
J = Point.Point([10,3])
E = Point.Point([5,2])
F = Point.Point([7,1])

Data = [A, B, C, D, G, J, E, F]

I = Point.Point([3,4.5])
EF = Point.Point([6, 1.5])
H = Point.Point([9, 5])

Centers = [I, EF, H]

print (Distortion(Data, Centers))
