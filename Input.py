import Print
import random

#Asks the user to define first point to be the first center
def EnterFirstCenter(Points):
	answer = ""
	firstPointIndex = -1
	outOfRange = False
	
	while ((answer != "yes" and answer != "no") or outOfRange):
		
		answer = input("Whether you prefer to define the initial point? (type yes or no) ");
		
		if answer == "no": 
			firstPointIndex = random.randint(0, len(Points)-1)
		elif answer == "yes":
			Print.PrintPoints(Points)
			try:
				firstPointIndex = int(input("Type index of initial point from list above: "))-1
			except ValueError:
				print("Index is not a integer, try again.")
				outOfRange = True
				continue
			if firstPointIndex not in range(0, len(Points)):
				print("Index out of range, try again.");
				outOfRange = True
			else:
				outOfRange = False
		else:
			print("You didn't enter neither yes neither no, try again.")
	return firstPointIndex
	