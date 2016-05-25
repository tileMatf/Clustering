import random

#randomly choice index with probability choice
def WeightedChoice(choices):
	total = sum(choices)
	r = random.uniform(0, total)
	upto = 0
	for i in range(0, len(choices)):
		if upto + choices[i] >= r:
			return i
		upto += choices[i]
	assert False, "Shouldn't get here"

"""
choices = [0.1, 0.4, 0.5]
print (WeightedChoice(choices)) 
"""
