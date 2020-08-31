import random


def primary():
	

	f = open("quotes.txt")
	quotes = f.readlines()
	f.close()

	last = 13
	rnd = random.randint(0, last)
	#The last variable holds the highest index for the array. Then our random number is 
	#stored in rnd using the random.randint function, which takes the lowest-possible 
	#number (zero) and the highest-possible number (stored in last).


	#Instead of including a number between the brackets, 
	#we'll put our random number variable:
	print(quotes[rnd])

if __name__== "__main__":
	primary()
