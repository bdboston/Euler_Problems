# Project Euler, Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

### Find all the numbers from 1 to 999 that are multiples of 3 or 5 and add them to find thier sum. ###
total_1 = 0
for n in range(1, 1000):
	if n % 3 == 0:
		total_1 += n
	elif n % 5 == 0:
		total_1 += n
print(total)


### Let do that a second way. ###
total_2 = 0
for n in range(1, 1000):
	if n % 3 == 0 or n % 5 == 0:
		total_2 += n
print(total_2)


### Let's try it a third way uning ranges to generate the multiples. ###
multiples_of_three = set(range(0,1000,3))
multiples_of_five = set(range(0,1000,5))
multiples_of_three_or_five = multiples_of_three.union(multiples_of_five)
total_3 = 0
for n in multiples_of_three_or_five:
	total_3 += n
print(total_3)
	
