import numpy as np

# weight = float(input("How many pounds does your suitcase weigh? "))
# if weight > 50:
# 	print ("Your suitcase weighs more than 50 lbs")
# else:
# 	print ("Your suitcase weighs less than 50 lbs")

"""
temperature = float(input('What is the temperature? '))
weather = input('What is the weather? (rain or shine) ')

if temperature > 60:
	if weather == "rain":
		print ("Bring an umbrella")
	else:
		print ("Wear a t-shirt")
else:
	if weather == "rain":
		print ("Bring an umbrella and jacket")
	else:
		print ("Bring a jacket")	

for i in range(1,16):
	print (i)	"""

with open('./datasets/coffee-preferences.csv','r') as f:
	lines = f.readlines()
for i in range(0,11):
	print (lines[i])
