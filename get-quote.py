import random


def primary():
	#Here we are opening the quotes.txt file, 
	#reading all the lines into a new variable called quotes,
	#then closing the file (defined by the variable f). Finally, 
	#we print out the quotes.

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
	quote_output = quotes[rnd]

	quote_output = quote_output.rstrip("\n")

	print(quote_output)


if __name__== "__main__":
	primary()
